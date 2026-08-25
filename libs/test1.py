
from langchain_core.messages import HumanMessage

for n in (2,4):
    msgs = [HumanMessage([{"type": "text", "text": f"m{i}"}]) for i in range(n)]
    print(msgs)

