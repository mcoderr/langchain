from langchain_core.exceptions import (
    OutputParserException,
    ModelRateLimitError,
    ContextOverflowError,
)
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o")

try:
    response = llm.invoke("..." * 100000)  # Exceed context window
except ContextOverflowError:
    print("Input too long! Truncating and retrying...")

except ModelRateLimitError:
    print("Rate limited — backing off and retrying...")

except OutputParserException as e:
    print(f"Could not parse output: {e}")