from langchain_core.utils.function_calling import convert_to_openai_tool
from langchain_core.utils import from_env
from langchain_core.utils.json import parse_partial_json
from pydantic import BaseModel

# Convert a Pydantic model to OpenAI tool schema
class SearchQuery(BaseModel):
    query: str
    max_results: int = 5

tool_schema = convert_to_openai_tool(SearchQuery)
# Produces the JSON schema OpenAI expects for function calling

# Safe environment variable access
api_key = from_env("OPENAI_API_KEY", default="")

# Parse incomplete JSON (common during streaming)
partial = '{"name": "Alice", "age": 30, "hobbies": ["reading"'
result = parse_partial_json(partial)
# result == {"name": "Alice", "age": 30, "hobbies": ["reading"]}