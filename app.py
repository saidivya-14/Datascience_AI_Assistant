import streamlit as st


st.title("Data science AI Assistant")
query = st.text_area("Enter your doubts")
btn_click = st.button("Answer Query")


import google.generativeai as ai
ai.configure(api_key= "enter your API key")
admin_prompt = """you are a helpful assistant which answers user's query.note that you anly answer data science related queries from user.
in case user asks a query outside of the datascience politely tell the use to enter data science related query"""
model = ai.GenerativeModel(model_name="models/gemini-1.5-flash",system_instruction = admin_prompt)




if btn_click == True:
    response = model.generate_content(query)
    st.write(response.text)