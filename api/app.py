from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv
from langchain_community.llms import ollama
load_dotenv()
app = FastAPI(title="LangServe API", description="API for LangServe", version="1.0.0")
add_routes(app,
           ChatOpenAI(),
           path="/openai",
           )
model=ChatOpenAI(model="gpt-3.5-turbo")
prompt1=ChatPromptTemplate.from_template("write me an essay about some {topic} with 100 words ")

add_routes(app,prompt1|model,path="/essay")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)


