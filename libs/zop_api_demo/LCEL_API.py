from langchain_core.runnables import (
    RunnableLambda,
    RunnableParallel,
    RunnablePassthrough,
    RunnableBranch,
)
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o")

# --- Pipe operator: compose a chain ---
chain = (
    ChatPromptTemplate.from_template("Tell me a joke about {topic}")
    | llm
    | StrOutputParser()
)
result = chain.invoke({"topic": "cats"})

# --- RunnableParallel: run multiple branches simultaneously ---
chain = RunnableParallel(
    joke=ChatPromptTemplate.from_template("Tell a joke about {topic}") | llm | StrOutputParser(),
    poem=ChatPromptTemplate.from_template("Write a poem about {topic}") | llm | StrOutputParser(),
)
result = chain.invoke({"topic": "space"})
# result == {"joke": "...", "poem": "..."}

# --- RunnableLambda: wrap any function ---
def word_count(text: str) -> int:
    return len(text.split())

chain = llm | StrOutputParser() | RunnableLambda(word_count)
count = chain.invoke("Write a paragraph about AI")

# --- RunnableBranch: conditional routing ---
chain = RunnableBranch(
    (lambda x: "math" in x["topic"], math_chain),
    (lambda x: "code" in x["topic"], code_chain),
    default_chain,  # fallback
)

# --- Fallbacks: automatic retry with a different model ---
primary = ChatOpenAI(model="gpt-4o")
backup = ChatOpenAI(model="gpt-4o-mini")
llm_with_fallback = primary.with_fallbacks([backup])