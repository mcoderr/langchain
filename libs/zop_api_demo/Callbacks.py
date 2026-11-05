from langchain_core.callbacks import BaseCallbackHandler
from langchain_openai import ChatOpenAI

class TokenCounter(BaseCallbackHandler):
    def __init__(self):
        self.token_count = 0

    def on_llm_new_token(self, token: str, **kwargs):
        self.token_count += 1

    def on_llm_end(self, response, **kwargs):
        print(f"Total tokens streamed: {self.token_count}")

counter = TokenCounter()
llm = ChatOpenAI(model="gpt-4o", streaming=True, callbacks=[counter])
llm.invoke("Write a haiku about Python programming.")
# Output: Total tokens streamed: 23