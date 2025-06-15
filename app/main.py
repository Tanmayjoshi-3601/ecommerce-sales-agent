from fastapi import FastAPI
from app.graph import build_graph

app = FastAPI()
graph = build_graph()

@app.get("/ask")
def ask_agent(query:str):
    state = {"query":query}
    result = graph.invoke(state)
    return {"response": result["result"]}

