import streamlit as st
import Query_endpoint
import summary_endpoint

st.title("Summarizer App")

options = st.selectbox("Choose an option", ["Query", "Summarizer"])

if options == "Query":
    user_query = st.text_input("Enter your query")
    if user_query:  # Ensure the input is not empty
        query_response = Query_endpoint.qry(user_query)
        st.write(query_response)

elif options == "Summarizer":
    user_text = st.text_input("Enter your text")
    if user_text:  # Ensure the input is not empty
        summary_response = summary_endpoint.summary(user_text)
        st.write(summary_response)
