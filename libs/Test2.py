
from langchain_openai import ChatOpenAI

from langchain_core.prompts import PromptTemplate

llm = ChatOpenAI(temperature=0.9,api_key='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',verbose=True)
text = "What would be a good company name for a company that makes colorful socks?"
print(llm.invoke("""Solve this problem.

Give:
1. The answer
2. A concise explanation of the approach
3. The key steps used to reach the answer

Do not provide private chain-of-thought.
""").content)


prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?"
)

chain = prompt | llm

response = chain.invoke({
    "product": "eco-friendly water bottles"
})

print(response.content)
