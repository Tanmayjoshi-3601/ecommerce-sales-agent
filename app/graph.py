from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
from openai import OpenAI
from app.config import OPENAI_API_KEY
from typing import TypedDict
from app.tools import search_products
# client = OpenAI(api_key = OPENAI_API_KEY)

class AgentState(TypedDict):
    query: str
    result: str
    

def repeat_tool(state: AgentState) -> AgentState:
    query = state.get("query","")
    return {"result":f"You asked me {query}"}

def search_tool(state: AgentState) -> AgentState:
    query = state.get("query","")
    results = search_products(query)
    result_str = "\n".join([f"{p['title']} - ${p['price']}" for p in results])
    return {"result":result_str}

def build_graph():
    graph = StateGraph(AgentState)
    graph.add_node("ask_agent", search_tool)
    graph.set_entry_point("ask_agent")
    graph.set_finish_point("ask_agent")
    return graph.compile()


