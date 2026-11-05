from langchain_core.rate_limiters import InMemoryRateLimiter
from langchain_openai import ChatOpenAI

# Allow max 10 requests per second, bursting up to 20
rate_limiter = InMemoryRateLimiter(
    requests_per_second=10,
    check_every_n_seconds=0.1,
    max_bucket_size=20,
)

# Attach to a model
llm = ChatOpenAI(model="gpt-4o", rate_limiter=rate_limiter)

# Now even if you batch 100 requests, they'll be throttled automatically
responses = llm.batch(
    ["Question " + str(i) for i in range(100)],
    config={"max_concurrency": 20},
)