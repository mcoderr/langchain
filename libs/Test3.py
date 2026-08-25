from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain.agents import create_agent


# --------------------------------
# 1. Create the LLM
# --------------------------------

llm = ChatOpenAI(
    temperature=0,
    api_key='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'
)


# --------------------------------
# 2. Create our own tools
# --------------------------------

@tool
def get_employee_salary(name: str) -> float:
    """Return the annual salary of an employee."""

    employees = {
        "alice": 80000,
        "bob": 100000,
        "charlie": 120000
    }

    salary = employees.get(name.lower())

    if salary is None:
        return 0

    return salary


@tool
def calculate_bonus(salary: float) -> float:
    """Calculate a 10% bonus from an annual salary."""

    return salary * 0.10


# --------------------------------
# 3. Give tools to the agent
# --------------------------------

tools = [
    get_employee_salary,
    calculate_bonus
]


# --------------------------------
# 4. Create the agent
# --------------------------------

agent = create_agent(
    model=llm,
    tools=tools
)


# --------------------------------
# 5. Ask the agent a question
# --------------------------------

result = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "What is Alice's salary and how much bonus will she receive?"
        }
    ]
})


# --------------------------------
# 6. Print final response
# --------------------------------

print(result["messages"][-1].content)