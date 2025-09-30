# AI-based UFDR Analysis Tool Prototype 🕵️

A prototype application that leverages Large Language Models (LLMs) to analyze Universal Forensic Extraction Device Reports (UFDRs) using natural language queries. This tool is designed to help investigating officers quickly find actionable intelligence from massive datasets without needing technical expertise.


---

## ## The Problem

Digital forensic reports (UFDRs) contain huge amounts of data like chats, calls, and contacts. Manually sifting through this data is slow, tedious, and can delay investigations. This tool solves that problem by providing an intelligent, easy-to-use interface for data analysis.

---

## ## Features ✨

* **Natural Language Queries:** Ask questions in plain English (e.g., "Show me chats containing 'crypto'").
* **AI-Powered Analysis:** Uses an AI backend (like Google Gemini or OpenAI) to understand the user's query and generate the appropriate data filtering code on the fly.
* **Simple Web Interface:** Built with Streamlit for a clean and intuitive user experience.
* **Handles Mock Data:** Demonstrates the concept using sample CSV files for chats, calls, and contacts.

---

## ## Tech Stack 🛠️

* **Language:** Python
* **Framework:** Streamlit
* **Data Handling:** Pandas
* **AI Backend:** Google Gemini API / OpenAI API

---

## ## Setup and Installation

Follow these steps to run the project locally on your machine.

**1. Clone the Repository:**
```bash
git clone [https://github.com/YourUsername/AI-based-UFDR---Prototype.git](https://github.com/YourUsername/AI-based-UFDR---Prototype.git)
cd AI-based-UFDR---Prototype
```
**2. Create and Activate a Virtual Environment:**
```bash
# Create the environment
python -m venv .venv

# Activate on Windows
.\.venv\Scripts\Activate

# Activate on macOS/Linux
# source .venv/bin/activate
```

**3. Install Dependencies:**
```bash
pip install -r requirements.txt
```

**4. Add Your API Key:**
   * Create a new folder in the root directory named `.streamlit`.
   * Inside the `.streamlit` folder, create a new file named `secrets.toml`.
   * Open `secrets.toml` and add your API key like this (use either a Gemini or OpenAI key depending on the version of `app.py` you are using):
     ```toml
     # For Google Gemini
     GEMINI_API_KEY = "your-google-api-key-here"

     # Or for OpenAI
     # OPENAI_API_KEY = "your-openai-api-key-here"
     ```

**5. Run the Application:**
```bash
streamlit run app.py
```
The application will open in your web browser!

---

## ## How to Use

Once the application is running:
1.  View the sample data in the "View Raw Data" expander if you wish.
2.  Type a question about the data into the text box (e.g., `Find calls longer than 200 seconds`).
3.  Click the **Analyze** button.
4.  The AI-generated code and the resulting data table will appear on the screen.
