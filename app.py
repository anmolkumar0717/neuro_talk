import streamlit as st
from google import genai
from gtts import gTTS
import uuid
import base64
import os

client = genai.Client()

st.set_page_config(page_title="AnmolAI Gemini Chat", page_icon="🤖")
st.title("🤖 AnmolAI – Gemini Chat + Voice Output")

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

    # -------------------------
    # 🔊 TEXT-TO-SPEECH (AUTO-PLAY ON BUTTON CLICK)
    # -------------------------
    tts_text = "Answer from Anmol AI is " + answer
    tts = gTTS(text=tts_text, lang="en")

    file_id = str(uuid.uuid4())
    file_name = f"audio_{file_id}.mp3"
    tts.save(file_name)

    # Encode to base64
    with open(file_name, "rb") as f:
        audio_bytes = f.read()
        audio_b64 = base64.b64encode(audio_bytes).decode()

    # Autoplay allowed because user clicked the "Send" button
    audio_html = f"""
    <audio autoplay>
        <source src="data:audio/mp3;base64,{audio_b64}" type="audio/mp3">
    </audio>
    """
    st.markdown(audio_html, unsafe_allow_html=True)

    # Optional: delete old audio files (cleanup)
    for f in os.listdir():
        if f.startswith("audio_") and f != file_name:
            os.remove(f)
