from langchain_core.prompts import (
    ChatPromptTemplate,
    FewShotChatMessagePromptTemplate,
    MessagesPlaceholder,
)

# Basic chat prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that speaks {language}."),
    ("human", "{question}"),
])
messages = prompt.invoke({"language": "French", "question": "What is AI?"})

# With message history placeholder
prompt_with_history = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder("chat_history"),   # Injects prior messages here
    ("human", "{input}"),
])

# Few-shot prompting
examples = [
    {"input": "2+2", "output": "4"},
    {"input": "3+3", "output": "6"},
]
example_prompt = ChatPromptTemplate.from_messages([
    ("human", "{input}"),
    ("ai", "{output}"),
])
few_shot = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=examples,
)

final_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a math tutor."),
    few_shot,
    ("human", "{question}"),
])
messages = final_prompt.invoke({"question": "5+5"})