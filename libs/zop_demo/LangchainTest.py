
from re import A, I
import time


from langchain_core.messages import HumanMessage
from langchain_core.messages.utils import merge_message_runs



for n in (500, 1000, 2000, 4000):
    msgs = [HumanMessage([{"type": "text", "text": f"m{i}"}]) for i in range(n)]
    start = time.perf_counter()
    merge_message_runs(msgs)
    print(n, round(time.perf_counter() - start, 3), "s")


"""
from langchain_core.messages import HumanMessage

msg = HumanMessage(content="Hello")
print(msg)





from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


import sys
from pathlib import Path

repo = Path(__file__).resolve().parent

sys.path.insert(0, str(repo / "partners" / "openai"))
sys.path.insert(0, str(repo.parent / "core"))   # if langchain_core is also local


from partners.openai.langchain_openai import ChatOpenAI

from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage,
)


# 1. Initialize the model
model = ChatOpenAI(model="gpt-4o",api_key="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") # type: ignore

# 2. Build the message history list
messages = [
    SystemMessage(content="You are a strict code reviewer. Be concise."),
    HumanMessage(content="Is my Python function optimized?"),
    AIMessage(content="No. Use a list comprehension instead of a loop."),
    HumanMessage(content="Show me how.")
]

# 3. Invoke the model
response = model.invoke(messages)
print(response.content)


"""
