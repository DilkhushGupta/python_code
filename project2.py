import streamlit as st
from langchain_groq import ChatGroq

llm = ChatGroq(
        model="gemma2-9b-it",
        temperature=0,
        groq_api_key="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"  # Replace with your actual API key
    )

prompt = f"Check the grammar of the following text.If it's correct, return it as is. If it has grammar mistakes, correct them without changing the meaning or adding extra words.Also, list the incorrect words and provide feedback on what went wrong.\nText: {text}"

response = llm.invoke(prompt)  # Get AIMessage object
corrected_text = response.content  # Extract actual text

st.title("Grammar Checker")
st.write("Enter your sentences below : ")
user_input = st.text_input("Your Question : ", "")

if st.button("Check Grammar"):
  response = llm.invoke(user_input)
  st.write("### Response:")
  st.write(response.content)