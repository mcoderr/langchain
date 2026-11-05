from langchain_core.load import dumps, loads, dumpd, load
from langchain_core.prompts import ChatPromptTemplate

# Create a prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a {role}."),
    ("human", "{question}"),
])

# Serialize to JSON string
json_str = dumps(prompt)
print(json_str)  # JSON representation of the prompt

# Serialize to dict
json_dict = dumpd(prompt)

# Deserialize back
restored_prompt = loads(json_str)
restored_prompt_2 = load(json_dict)

# Use the restored prompt
result = restored_prompt.invoke({"role": "teacher", "question": "What is gravity?"})