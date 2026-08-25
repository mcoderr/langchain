from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

@tool
def get_weather(city: str) -> str:
    """Get the current weather for a city."""
    return f"72°F and sunny in {city}"


model = ChatOpenAI(model="gpt-4o",api_key='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')

agent = create_agent(model,tools=[get_weather])
result = agent.invoke({"messages": [("user", "What's the weather in SF?")]})
print(result)