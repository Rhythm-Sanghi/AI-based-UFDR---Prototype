import streamlit as st
import pandas as pd
from openai import OpenAI
import os

try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except Exception as e:
    st.error("Please set your OPENAI_API_KEY in .streamlit/secrets.toml")
    st.stop()

st.title("AI Forensic Analysis Tool ")
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
        system_prompt = """
        You are a Python data analyst. Your job is to write a single line of Python code to answer a question.
        You have a Python dictionary named 'dataframes' which contains three pandas DataFrames: 'chats', 'calls', and 'contacts'.
        The columns are:
        - chats: ['timestamp', 'sender', 'receiver', 'message']
        - calls: ['timestamp', 'caller', 'receiver', 'duration_seconds']
        - contacts: ['name', 'number']
        
        Based on the user's question, you must write one line of Python code to find the answer.
        IMPORTANT: Only output the code itself, with no explanation or other text.
        """

        with st.spinner("AI is thinking..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_question}
                    ]
                )
                
                ai_generated_code = response.choices[0].message.content.strip()
                
                st.info(f"AI Generated this code: `{ai_generated_code}`")

                result = eval(ai_generated_code, {"pd": pd, "dataframes": dataframes})

                st.subheader("Here is the answer:")
                st.dataframe(result)

            except Exception as e:
                st.error(f"Something went wrong! Error: {e}")
                st.warning("The AI might have made a mistake. Try asking your question in a different way.")
    else:
        st.warning("Please type a question first!")