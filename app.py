import streamlit as st
import pandas as pd
import google.generativeai as genai

# Configure API key from .streamlit/secrets.toml
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
except Exception as e:
    st.error(f"API key configuration failed: {e}")
    st.stop()

st.title("AI Forensic Analysis Tool")
st.write("Ask a question about the data, and the AI will explain the answer in plain English.")

# Load datasets
try:
    chats_df = pd.read_csv("data/chats.csv")
    calls_df = pd.read_csv("data/calls.csv")
    contacts_df = pd.read_csv("data/contacts.csv")
    dataframes = {"chats": chats_df, "calls": calls_df, "contacts": contacts_df}

    with st.expander("Show raw data"):
        st.dataframe(chats_df)
        st.dataframe(calls_df)
        st.dataframe(contacts_df)
except FileNotFoundError:
    st.error("Error: Missing 'data' folder or CSV files.")
    st.stop()

# Input box
user_question = st.text_input(
    "Ask a question:",
    placeholder="Example: Who talks the most about crypto?"
)

if st.button("Analyze"):
    if user_question:
        try:
            # Prepare context: convert DataFrames to strings
            context = (
                "Chats:\n" + chats_df.head(20).to_string(index=False) + "\n\n" +
                "Calls:\n" + calls_df.head(20).to_string(index=False) + "\n\n" +
                "Contacts:\n" + contacts_df.head(20).to_string(index=False)
            )

            prompt = f"""
            You are a forensic data analyst. 
            You will be given three datasets: chats, calls, and contacts.
            Use them to answer the user's question in clear, plain English. 
            Do not output code. Just explain the answer simply.

            User's question: "{user_question}"

            Here is the available data (showing only first 20 rows for each):
            {context}
            """

            model = genai.GenerativeModel("gemini-2.5-flash")
            response = model.generate_content(prompt)

            st.subheader("Answer")
            st.write(response.text)

        except Exception as e:
            st.error(f"Analysis failed: {e}")
    else:
        st.warning("Please type a question first.")