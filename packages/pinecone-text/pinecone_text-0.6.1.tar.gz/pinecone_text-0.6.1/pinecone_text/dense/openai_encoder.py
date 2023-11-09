from typing import Union, List
from pinecone_text.dense.base_dense_ecoder import BaseDenseEncoder

try:
    import openai
except (OSError, ImportError, ModuleNotFoundError) as e:
    _openai_installed = False
else:
    _openai_installed = True


class OpenAIEncoder(BaseDenseEncoder):
    """
    OpenAI's text embedding wrapper. See https://platform.openai.com/docs/guides/embeddings

    Note: You should provide an API key and organization in the environment variables OPENAI_API_KEY and OPENAI_ORG.
    """

    def __init__(self, model_name: str = "text-embedding-ada-002"):
        if not _openai_installed:
            raise ImportError(
                "Failed to import openai. Make sure you install openai extra "
                "dependencies by running: "
                "`pip install pinecone-text[openai]"
            )
        self._model_name = model_name

    def encode_documents(
        self, texts: Union[str, List[str]]
    ) -> Union[List[float], List[List[float]]]:
        return self._encode(texts)

    def encode_queries(
        self, texts: Union[str, List[str]]
    ) -> Union[List[float], List[List[float]]]:
        return self._encode(texts)

    def _encode(
        self, texts: Union[str, List[str]]
    ) -> Union[List[float], List[List[float]]]:
        if isinstance(texts, str):
            texts_input = [texts]
        elif isinstance(texts, list):
            texts_input = texts
        else:
            raise ValueError(
                f"texts must be a string or list of strings, got: {type(texts)}"
            )

        try:
            response = openai.Embedding.create(input=texts_input, model=self._model_name)  # type: ignore
        except openai.error.OpenAIError as e:
            # TODO: consider wrapping external provider errors
            raise e
        if isinstance(texts, str):
            return response["data"][0]["embedding"]
        return [result["embedding"] for result in response["data"]]
