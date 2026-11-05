from langchain_core.embeddings import Embeddings

# The interface that all embedding providers implement
class Embeddings:
    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        """Embed a list of documents."""
        ...

    def embed_query(self, text: str) -> list[float]:
        """Embed a single query."""
        ...

# With a real provider (e.g., OpenAI):
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# Embed documents for indexing
doc_vectors = embeddings.embed_documents([
    "LangChain is a framework for LLM apps.",
    "Python is a programming language.",
])

# Embed a query for searching
query_vector = embeddings.embed_query("What is LangChain?")
# query_vector is a list of floats like [0.012, -0.034, 0.056, ...]