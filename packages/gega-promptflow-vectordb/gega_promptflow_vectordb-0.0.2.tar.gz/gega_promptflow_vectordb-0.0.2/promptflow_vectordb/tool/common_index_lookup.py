from .contracts.telemetry import StoreToolEventCustomDimensions
from .utils.logging import ToolLoggingUtils
from .utils.pf_runtime_utils import PromptflowRuntimeUtils

from ..core.logging.utils import LoggingUtils, StoreLogger

from azureml.rag.mlindex import MLIndex
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from io import StringIO
import os
from promptflow import tool
from typing import Any, Dict, List, Union
import uuid
import yaml


DISABLE_AZUREML_RAG_ENVVAR_KEY = "AZUREML_DISABLE_RAG_SDK"
__disable_azureml_rag = os.getenv(DISABLE_AZUREML_RAG_ENVVAR_KEY, "false").lower() in {"true", "1"}


search_executor = ThreadPoolExecutor()
logging_config = ToolLoggingUtils.generate_config(
    tool_name="promptflow_vectordb.tool.common_index_lookup"
)


@tool
def search(
    mlindex_content: str,
    queries: Union[str, List[str]],
    top_k: int
) -> List[List[dict]]:
    logger = LoggingUtils.sdk_logger(__package__, logging_config)
    logger.update_telemetry_context({
        StoreToolEventCustomDimensions.TOOL_INSTANCE_ID: str(uuid.uuid4())
    })

    if isinstance(queries, str):
        queries = [queries]

    try:
        pf_context = PromptflowRuntimeUtils.get_pf_context_info_for_telemetry()
    except Exception:
        pf_context = None
    
    if __disable_azureml_rag:
        return _perform_legacy_search(mlindex_content, queries, top_k, logger, pf_context)
    
    mlindex_config = yaml.safe_load(StringIO(mlindex_content))
    index = MLIndex(mlindex_config=mlindex_config)
    search_func = partial(index.as_langchain_vectorstore().similarity_search_by_vector_with_relevance_scores, top_k=top_k)

    search_results = search_executor.map(search_func, queries)
    return [[{**doc.as_dict(), 'score': score} for doc, score in search_result] for search_result in search_results]


def _perform_legacy_search(
        mlindex_content: str,
        queries: List[str],
        top_k: int,
        logger: StoreLogger,
        pf_context: Dict[str, Any]) -> List[List[dict]]:
    raise NotImplementedError()
