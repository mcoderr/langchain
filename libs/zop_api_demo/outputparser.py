from langchain_core.output_parsers import PydanticOutputParser, JsonOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

# Define your desired output structure
class Movie(BaseModel):
    title: str = Field(description="The movie title")
    director: str = Field(description="The director's name")
    year: int = Field(description="Release year")
    rating: float = Field(description="Rating out of 10")

# Create a parser
parser = PydanticOutputParser(pydantic_object=Movie)

# The parser generates format instructions for the prompt
prompt = PromptTemplate(
    template="Suggest a great sci-fi movie.\n{format_instructions}",
    input_variables=[],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

# Chain it together
from langchain_openai import ChatOpenAI
chain = prompt | ChatOpenAI(model="gpt-4o") | parser

movie: Movie = chain.invoke({})
print(movie.title)     # e.g., "Blade Runner 2049"
print(movie.year)      # e.g., 2017

# Simple string parsing (most common for streaming)
from langchain_core.output_parsers import StrOutputParser
chain = ChatOpenAI() | StrOutputParser()
result: str = chain.invoke("Say hello")