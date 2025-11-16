import streamlit as st
from google import genai
from gtts import gTTS
import uuid
import base64
import os

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

st.set_page_config(page_title="AnmolAI, page_icon="🤖")
st.title("🤖 Anmol-AI")

user_input = st.text_input("You:", placeholder="Type your message...")
send_button = st.button("Send")

if send_button and user_input:
    with st.spinner("Thinking..."):
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_input
        )

    answer = response.text

    st.markdown("### 💬 AnmolAI:")
    st.write(answer)

