from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from langchain_core.runnables import RunnableParallel
from langchain_core.runnables import RunnablePassthrough



model = ChatOpenAI(model="gpt-4o-mini", temperature=0,api_key='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')


def runnable_lamda():
    #this function is use to inject runnable interfae llm
    my_step = RunnableLambda(lambda x: x.upper())
    prompt = PromptTemplate.from_template(
                "Explain {topic} in simple terms."
            )
    chain = prompt | model | StrOutputParser() | my_step

    result = chain.invoke({
        "topic": "RunnableLambda"
    })

    print(result)



def ruunable_parallel():

     #this function is use to current parallel PromptTemplate

    summary_prompt = PromptTemplate.from_template(
        "Summarize this review in one sentence:\n{review}"
    )

    sentiment_prompt = PromptTemplate.from_template(
        "Determine the sentiment of this review. "
        "Return only Positive, Negative, or Neutral:\n{review}"
    )

    keywords_prompt = PromptTemplate.from_template(
        "Extract 3 important keywords from this review:\n{review}"
    )

    chain = RunnableParallel(
        summary=summary_prompt | model,
        sentiment=sentiment_prompt | model,
        keywords=keywords_prompt | model,
    )

    result = chain.invoke({
        "review": "The phone has an excellent camera and battery life, "
                "but the UI is sometimes slow."
    })

    print(result)



def ruunable_parallel():

    chain = RunnablePassthrough.assign(context=retriever) | prompt | model



#runnable_lamda()

ruunable_parallel()