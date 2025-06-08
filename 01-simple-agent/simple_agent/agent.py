from google.adk.agents import Agent
from google.adk.tools import google_search

def get_sa_markup(quote: int) -> dict:
    """
    Calculate the SA markup for a given quote.
    """
    return {
        "SA_markup": quote*1.30,
    }

root_agent = Agent(
    name="simple_agent",
    model="gemini-2.0-flash",
    description="Simple Tool calling agent",
    instruction="""
    You are a helpful assistant that can use the following tools:
    - google_search
    """,
    tools=[google_search],
   # tools=[get_sa_markup],
    # tools=[google_search, get_sa_markup], # <- This won't work - can't mix default tool with function tool
)
