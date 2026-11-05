import time

from langchain_core.messages import HumanMessage
from langchain_core.messages.utils import merge_message_runs

def normal_test():
    for n in (2,4):
        msgs = [HumanMessage([{"type": "text", "text": f"m{i}"}]) for i in range(n)]
        print(msgs)

def error_reproduce():
    for n in (500, 1000, 2000, 4000,8000):
        msgs = [HumanMessage([{"type": "text", "text": f"m{i}"}]) for i in range(n)]
        start = time.perf_counter()
        merge_message_runs(msgs)
        elapsed = time.perf_counter() - start
        print(f"{n:5d} messages -> {elapsed:.3f}s")



error_reproduce()