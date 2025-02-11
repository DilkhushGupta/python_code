import streamlit as st
from langchain_groq import ChatGroq

llm = ChatGroq(
  model = "mixtral-8x7b-32768",
  temperature=0,
  groq_api_key = "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"
)

st.title("Simple LLM Chatbot")
st.write("Enter your query below : ")
user_input = st.text_input("Your Question : ", "")

if st.button("Get Answer"):
  response = llm.invoke(user_input)
  st.write("### Response:")
  st.write(response.content)