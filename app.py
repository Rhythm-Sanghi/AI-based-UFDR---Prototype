import streamlit as st
import pandas as pd
import google.generativeai as genai
import os

try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except:
    st.error("Error: Make sure your GEMINI_API_KEY is set in .streamlit/secrets.toml!")
    st.stop()

st.title(" AI Forensic Analysis Tool")
st.write("AI will find the answers in the data.")

try:
    chats_df = pd.read_csv("data/chats.csv")
    calls_df = pd.read_csv("data/calls.csv")
    contacts_df = pd.read_csv("data/contacts.csv")

    dataframes = {
        "chats": chats_df,
        "calls": calls_df,
        "contacts": contacts_df
    }

    with st.expander("Click here to see the raw data"):
        st.write("Chats Data:")
        st.dataframe(chats_df)
        st.write("Calls Data:")
        st.dataframe(calls_df)
        st.write("Contacts Data:")
        st.dataframe(contacts_df)

except FileNotFoundError:
    st.error("Error: Make sure your 'data' folder and CSV files exist!")
    st.stop()

user_question = st.text_input(
    "Ask a question about the data:", 
    placeholder="e.g., Show me chats that mention 'crypto'"
)

if st.button("Analyze"):
    if user_question:
        prompt = f"""
        You are a Python data analyst. Write a single line of Python code to answer a question.
        You have a dictionary of pandas DataFrames called 'dataframes'. The keys are 'chats', 'calls', and 'contacts'.
        - chats columns: ['timestamp', 'sender', 'receiver', 'message']
        - calls columns: ['timestamp', 'caller', 'receiver', 'duration_seconds']
        - contacts columns: ['name', 'number']
        
        Based on the user's question, write one line of Python code to find the answer.
        Only output the code itself.

        User's question: "{user_question}"
        Python code:
        """

        with st.spinner("The AI is thinking..."):
            try:
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(prompt)
                ai_generated_code = response.text.strip()
                
                st.info(f"AI Generated this code: `{ai_generated_code}`")

                result = eval(ai_generated_code, {"pd": pd, "dataframes": dataframes})

                st.subheader("Here is the answer:")
                st.dataframe(result)

            except Exception as e:
                st.error(f"Something went wrong! Error: {e}")
                st.warning("The AI might have made a mistake. Try asking your question in a different way.")
    else:
        st.warning("Please type a question first!")