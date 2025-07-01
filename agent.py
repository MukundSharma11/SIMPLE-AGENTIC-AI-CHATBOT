import os
from dotenv import load_dotenv
load_dotenv()
from langgraph.prebuilt import create_react_agent
from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages
from langchain_core.messages import AIMessage, HumanMessage
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch

GROQ_API_KEY = os.getenv('GROQ_API_KEY')
TAVILY_API_KEY = os.getenv('TAVILY_API_KEY')
LANGSMITH_API_KEY = os.getenv('LANGSMITH_API_KEY')

# llm = ChatGroq(model = 'gemma2-9b-it', max_tokens= 100)
# tavily = TavilySearch(max_results = 2)

# class State(TypedDict):
#     messages: Annotated[list, add_messages]
# State['messages'] = "Recent AI news"

# query = "Hello!"
# response = agent.invoke({
#     "messages": [HumanMessage(content=query)]
# })
# messages = response.get('messages')
# ai_message = [msg for msg in messages if isinstance(msg, AIMessage)]
# print(messages)
# # print(ai_message[-1].content)

def get_response_from_ai_agent(llm_name, allow_search, prompt, query):
    
    tools = [TavilySearch(max_results = 2)] if allow_search else []
    
    llm = ChatGroq(model = llm_name, max_tokens= 100)
    
    agent = create_react_agent(
    model = llm,
    tools=tools,
    prompt= prompt
)
    query = query
    response = agent.invoke({
        "messages": [HumanMessage(content=query)]
    })
    messages = response.get('messages')
    ai_message = [msg for msg in messages if isinstance(msg, AIMessage)]
    return ai_message[-1].content