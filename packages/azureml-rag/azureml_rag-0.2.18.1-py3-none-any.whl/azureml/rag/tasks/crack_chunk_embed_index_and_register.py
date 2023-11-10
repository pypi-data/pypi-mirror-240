# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
import copy
import datetime
import json
import re
import os
import time
import traceback
from pathlib import Path
from typing import Dict, Optional, Union
from azureml.core import Run

from azureml.rag._asset_client.client import get_rest_client, register_new_data_asset_version
from azureml.rag.embeddings import EmbeddingsContainer
from azureml.rag.mlindex import MLIndex
from azureml.rag.tasks.crack_and_chunk_and_embed import crack_and_chunk_and_embed, str2bool
from azureml.rag.tasks.crack_and_chunk_and_embed_and_index import crack_and_chunk_and_embed_and_index
from azureml.rag.utils.logging import (
    _logger_factory,
    enable_appinsights_logging,
    enable_stdout_logging,
    get_logger,
    safe_mlflow_start_run,
    track_activity,
)

logger = get_logger("crack_chunk_embed_index_and_register")


def crack_chunk_embed_index_and_register(args, run, logger, activity_logger):
    """Main function for crack_chunk_embed_index_and_register."""

    if args.output_path is None:
        args.output_path = f"{Path.cwd()}/embeddings"

    mlindex = crack_and_chunk_and_embed_and_index(
        logger,
        activity_logger,
        source_uri=args.input_data,
        source_glob=args.input_glob,
        chunk_size=args.chunk_size,
        chunk_overlap=args.chunk_overlap,
        use_rcts=args.use_rcts,
        custom_loader=args.custom_loader,
        citation_url=args.citation_url,
        citation_replacement_regex=args.citation_replacement_regex,
        embeddings_model=args.embeddings_model,
        embeddings_connection=args.embeddings_connection_id,
        embeddings_cache=args.embeddings_container,
        index_type=args.index_type,
        index_connection=args.index_connection_id,
        index_config=json.loads(args.index_config),
        output_path=args.output_path,
        doc_intel_connection_id=args.doc_intel_connection_id
    )

    if "://" in args.asset_uri:
        from azureml.dataprep.fuse.dprepfuse import MountOptions, rslex_uri_volume_mount
        mnt_options = MountOptions(
            default_permission=0o555, read_only=False, allow_other=False, create_destination=True)
        mount_context = rslex_uri_volume_mount(args.asset_uri, f"{Path.cwd()}/mlindex_asset", options=mnt_options)
        mount_context.start()
        mlindex.save(mount_context.mount_point)


    # Register the MLIndex data asset
    if run:
        ws = run.experiment.workspace
        client = get_rest_client(ws)
        data_version = register_new_data_asset_version(
            client,
            run,
            args.asset_name,
            args.asset_uri,
            properties={
                "azureml.mlIndexAssetKind": args.index_type,
                "azureml.mlIndexAsset": "true",
                "azureml.mlIndexAssetSource": run.properties.get("azureml.mlIndexAssetSource", "Unknown"),
                "azureml.mlIndexAssetPipelineRunId": run.properties.get("azureml.pipelinerunid", "Unknown")
            })

        logger.info(f"Finished Registering MLIndex Asset '{args.asset_name}', version = {data_version.version_id}")
    else:
        logger.info(f"Skipping MLIndex Asset registration because no run context was provided")

    return mlindex



def main_wrapper(args, run, logger):
    with track_activity(logger, "crack_and_chunk_and_embed") as activity_logger, safe_mlflow_start_run(logger=logger):
        try:
            crack_chunk_embed_index_and_register(args, run, logger, activity_logger)
        except Exception as e:
            activity_logger.error(f"crack_and_chunk failed with exception: {traceback.format_exc()}")  # activity_logger doesn't log traceback
            raise e


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--input_data", type=str)
    parser.add_argument("--input_glob", type=str, default="**/*")
    parser.add_argument("--chunk_size", type=int)
    parser.add_argument("--chunk_overlap", type=int)
    parser.add_argument("--citation_url", type=str, required=False)
    parser.add_argument("--citation_replacement_regex", type=str, required=False)
    parser.add_argument("--custom_loader", type=str2bool, default=None)

    parser.add_argument("--embeddings_model", type=str, required=True)
    parser.add_argument("--embeddings_connection_id", type=str, required=False)
    parser.add_argument("--embeddings_container", type=str, required=False)
    parser.add_argument("--batch_size", type=int, default=-1)
    parser.add_argument("--num_workers", type=int, default=-1)

    parser.add_argument("--index_type", type=str, required=False, default="acs")
    parser.add_argument("--index_connection_id", type=str, required=False)
    parser.add_argument("--index_config", type=str, required=True)

    parser.add_argument("--asset_name", type=str, required=False)
    parser.add_argument("--asset_description", type=str, required=False)
    parser.add_argument("--asset_uri", type=str, required=False)
    parser.add_argument("--output_path", type=str)
    parser.add_argument("--doc_intel_connection_id", type=str, default=None, help="The connection id for Document Intelligence service")

    # Legacy
    parser.add_argument("--max_sample_files", type=int, default=-1)
    parser.add_argument("--use_rcts", type=str2bool, default=True)

    args = parser.parse_args()
    print("\n".join(f"{k}={v}" for k, v in vars(args).items()))

    enable_stdout_logging()
    enable_appinsights_logging()

    if args.embeddings_connection_id is None:
        logger.info("Reading connection id from environment variable")
        args.embeddings_connection_id = os.environ.get("AZUREML_WORKSPACE_CONNECTION_ID_AOAI")
    if args.index_connection_id is None:
        logger.info("Reading connection id from environment variable")
        args.index_connection_id = os.environ.get("AZUREML_WORKSPACE_CONNECTION_ID_ACS")

    run: Run = Run.get_context()

    try:
        main_wrapper(args, run, logger)
    finally:
        if _logger_factory.appinsights:
            _logger_factory.appinsights.flush()
            time.sleep(5)
