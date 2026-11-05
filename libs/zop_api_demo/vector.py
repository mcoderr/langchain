from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# Create an in-memory vector store
vector_store = InMemoryVectorStore(embedding=embeddings)

# Add documents
docs = [
    Document(page_content="LangChain makes building LLM apps easy."),
    Document(page_content="Vector stores enable semantic search."),
    Document(page_content="Python is widely used in data science."),
    Document(page_content="RAG combines retrieval with generation."),
]
vector_store.add_documents(docs)

# Similarity search — find most relevant documents
results = vector_store.similarity_search("How does RAG work?", k=2)
for doc in results:
    print(doc.page_content)

# Search with scores
results_with_scores = vector_store.similarity_search_with_score(
    "semantic search", k=2
)
for doc, score in results_with_scores:
    print(f"{score:.4f}: {doc.page_content}")

# Convert to a retriever for use in chains
retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3},
)

# Use in a RAG chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI

rag_chain = (
    {
        "context": retriever,
        "question": RunnablePassthrough(),
    }
    | ChatPromptTemplate.from_template(
        "Answer based on context:\n{context}\n\nQuestion: {question}"
    )
    | ChatOpenAI(model="gpt-4o")
    | StrOutputParser()
)

answer = rag_chain.invoke("What is RAG?")