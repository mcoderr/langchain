from langchain_core.messages import  HumanMessage
from langchain_openai import ChatOpenAI

# Reads OPENAI_API_KEY from the environment; do not hardcode API keys in source.
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0,api_key='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')

messages = []

# User
messages.append(
    HumanMessage(content="Hi there!")
)

response = llm.invoke(messages)
print("AI:", response.content)

# Add AI response to history
messages.append(response)

# User's next message
messages.append(
    HumanMessage(content="What did I just say?")
)

response = llm.invoke(messages)
print("AI:", response.content)
