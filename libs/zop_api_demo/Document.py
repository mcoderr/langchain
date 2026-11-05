from langchain_core.documents import Document

# Create documents manually
doc = Document(
    page_content="LangChain is a framework for building LLM-powered applications.",
    metadata={"source": "langchain_docs", "page": 1, "topic": "overview"}
)

print(doc.page_content)   # The text content
print(doc.metadata)       # {"source": "langchain_docs", "page": 1, ...}

# Documents are what loaders produce and retrievers return
docs = [
    Document(page_content="Python is a programming language.", metadata={"source": "wiki"}),
    Document(page_content="JavaScript runs in the browser.", metadata={"source": "wiki"}),
]


print(docs)

