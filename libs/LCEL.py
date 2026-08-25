from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

chain = ChatPromptTemplate.from_template("Tell me about {topic}") | ChatOpenAI(api_key='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') | StrOutputParser()
result = chain.invoke({"topic": "quantum computing"})

print(result)