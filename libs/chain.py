# --- Example 1: Basic chain (LCEL) ---
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{question}")
])
model = ChatOpenAI(model="gpt-4o",api_key='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')
parser = StrOutputParser()

chain = prompt | model | parser
answer = chain.invoke({"question": "What is LCEL?"})
print(answer)