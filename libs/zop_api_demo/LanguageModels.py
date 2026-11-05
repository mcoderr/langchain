from langchain_core.language_models import BaseChatModel
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# All chat model providers implement BaseChatModel
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o", temperature=0.7)

# invoke() — single call
response = llm.invoke([
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Explain quantum computing in one sentence."),
])
print(response.content)

# stream() — token-by-token streaming
for chunk in llm.stream("Tell me a joke"):
    print(chunk.content, end="", flush=True)

# batch() — parallel calls
responses = llm.batch([
    "Translate 'hello' to French",
    "Translate 'hello' to Spanish",
    "Translate 'hello' to Japanese",
])

# bind_tools() — attach tools for function calling
from langchain_core.tools import tool

@tool
def get_weather(city: str) -> str:
    """Get weather for a city."""
    return f"Sunny in {city}"

llm_with_tools = llm.bind_tools([get_weather])
response = llm_with_tools.invoke("What's the weather in Paris?")