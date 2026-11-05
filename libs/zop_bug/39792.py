from langchain_core.runnables import RunnableLambda, RunnableParallel, RunnablePassthrough

parallel = RunnableParallel(a=RunnablePassthrough(), b=RunnableLambda(lambda x: x))
schema = parallel.get_input_schema()

print(schema.model_json_schema())
# {'properties': {'root': {'title': 'Root'}}, 'required': ['root'], ...}

value = {"k": 1}
print(parallel.invoke(value))   # works: {'a': {'k': 1}, 'b': {'k': 1}}

#schema.model_validate(value)    # raises
