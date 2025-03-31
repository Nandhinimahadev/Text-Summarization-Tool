import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()
opeclient = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI(api_key=opeclient)


def summarize_text(input_text):
    """Generates a summary using GPT-4."""
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert summarizer."},
                {"role": "user", "content": input_text},
            ],
            max_tokens=200,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"


st.title("AI Text Summarizer")
st.write("Enter a text passage below, and AI will generate a summary.")

user_input = st.text_area("Enter text to summarize:", height=200)
if st.button("Summarize"):
    if user_input.strip():
        summary = summarize_text(user_input)
        st.subheader("Summary:")
        st.write(summary)
    else:
        st.warning("Please enter some text to summarize.")
