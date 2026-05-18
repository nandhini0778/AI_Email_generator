import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

st.set_page_config(page_title="Email Generator", page_icon="✉️", layout="wide")

st.title("AI Email Generator (Groq Powered)")
st.write("Generate professional emails using AI")

def get_api_key():
    key = os.getenv("GROQ_API_KEY")
    if key:
        return key
    try:
        return st.secrets["GROQ_API_KEY"]
    except Exception:
        return None

api_key = get_api_key()

if not api_key:
    st.error(" GROQ API key not found. Add it to secrets.toml or environment variables.")
    st.stop()


llm = ChatGroq(
    api_key=api_key,
    model="llama-3.1-8b-instant",
    temperature=0.7
)

# ---------------- SIDEBAR INPUTS ----------------
st.sidebar.header("Email Settings")

topic = st.sidebar.text_input(
    " Email Topic",
    placeholder="e.g., Project deadline, Sick leave, Meeting request"
)

tone = st.sidebar.selectbox(
    " Select Tone",
    ["Formal", "Friendly", "Professional"]
)


def generate_email(topic, tone):
    if not topic:
        return "Please enter a topic."

    prompt = f"""
Generate a professional email.

Requirements:
- Topic: {topic}
- Tone: {tone}
- 3–4 paragraphs
- Include greeting, body, and closing
- Use placeholders like [Recipient], [Your Name]
- No explanations, only email content
"""

    try:
        messages = [HumanMessage(content=prompt)]
        result = llm.invoke(messages)
        return result.content
    except Exception as e:
        return f"Error: {str(e)}"


if st.sidebar.button(" Generate Email", use_container_width=True):
    if not topic:
        st.error("Please enter a topic first!")
    else:
        with st.spinner("Generating email..."):
            email = generate_email(topic, tone)

        st.success("Email Generated!")

        st.subheader("Generated Email")
        st.text_area("", value=email, height=400)

        st.download_button(
            "⬇ Download Email",
            data=email,
            file_name="email.txt",
            mime="text/plain"
        )