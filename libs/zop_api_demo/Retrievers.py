from langchain_core.retrievers import BaseRetriever
from langchain_core.documents import Document
from langchain_core.callbacks import CallbackManagerForRetrieverRun
from typing import List

class KeywordRetriever(BaseRetriever):
    """Simple retriever that filters documents by keyword match."""
    documents: List[Document]

    def _get_relevant_documents(
        self, query: str, *, run_manager: CallbackManagerForRetrieverRun
    ) -> List[Document]:
        return [
            doc for doc in self.documents
            if query.lower() in doc.page_content.lower()
        ]

# Usage
docs = [
    Document(page_content="Python is great for data science."),
    Document(page_content="JavaScript powers the web."),
    Document(page_content="Python has many ML libraries."),
]

retriever = KeywordRetriever(documents=docs)
results = retriever.invoke("Python")
# Returns 2 documents containing "Python"

# More commonly, you use a vector store's built-in retriever:
# retriever = vector_store.as_retriever(search_kwargs={"k": 5})