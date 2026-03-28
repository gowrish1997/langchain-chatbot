from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import  streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"

prompt=ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant please response to the user query in a concise manner."),
        ("user", "Question: {question}")
    ]
)

## streamlit app
st.title("Langchain demo with OpenAI")
input_text=st.text_input("search the topic u want")

llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9, max_tokens=100)
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))

