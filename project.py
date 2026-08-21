import os
import tempfile

import streamlit as st
import speech_recognition as sr

from pydub import AudioSegment as AS
from dotenv import load_dotenv
from google import genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    st.error("GEMINI_API_KEY not found. Please add it to your .env file.")
    st.stop()

client = genai.Client(api_key=GEMINI_API_KEY)


st.set_page_config(
    page_title="Meeting Summarizer",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'Poppins', sans-serif;
        }

        .main-title {
            text-align: center;
            color: grey;
            font-size: 40px;
            font-weight: 700;
        }

        .sub-title {
            text-align: center;
            color: white;
            font-size: 18px;
            font-weight: 400;
        }
    </style>
    """,
    unsafe_allow_html=True
)

def transcriber(uploaded_file):

    file_path = None

    try:
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".wav"
        ) as tmpfile:

            file_path = tmpfile.name
            audio_bytes = uploaded_file.read()
            temp_input = tempfile.NamedTemporaryFile(
                delete=False
            )

            temp_input.write(audio_bytes)
            temp_input.close()

            input_path = temp_input.name

        audio = AS.from_file(input_path)

        # Convert audio to suitable format
        audio = (
            audio
            .set_frame_rate(16000)
            .set_channels(1)
            .set_sample_width(2)
        )

        # Export as WAV
        audio.export(
            file_path,
            format="wav"
        )

        # Remove temporary input file
        os.remove(input_path)

        # Display audio
        st.audio(
            audio_bytes,
            format=uploaded_file.type
        )

        # Speech recognizer
        recognizer = sr.Recognizer()

        with sr.AudioFile(file_path) as source:

            st.info("Transcribing audio... Please wait.")

            audio_data = recognizer.record(source)

        try:

            text = recognizer.recognize_google(
                audio_data
            )

            st.success(
                "Transcription completed successfully."
            )

            return text

        except sr.UnknownValueError:

            st.error(
                "Could not understand the audio."
            )

            return "error"

        except sr.RequestError:

            st.error(
                "Google Speech Recognition API error. "
                "Please check your internet connection."
            )

            return "error"

    except Exception as e:

        st.error(
            f"Error while processing audio: {str(e)}"
        )

        return "error"

    finally:

        if file_path and os.path.exists(file_path):
            os.remove(file_path)


# ---------------------------------------------------------
# LLM SUMMARY
# ---------------------------------------------------------

def llm_summary(text):

    prompt = f"""
You are a professional meeting summarization assistant.

Analyze the meeting transcript provided below and create a
clear, professional and easy-to-read summary.

Your response must contain the following sections:

1. Overall Summary
   - Give a concise summary of the entire meeting.

2. Key Discussion Points
   - List the most important topics discussed.

3. Decisions Made
   - Mention the important decisions taken during the meeting.
   - If no decision was made, write "No major decisions were made."

4. Action Items
   - Mention tasks that need to be completed.
   - Include the responsible person if the transcript mentions one.

5. Deadlines and Follow-ups
   - Mention deadlines, future meetings or follow-up activities.
   - If none are mentioned, write "No specific deadlines or follow-ups were mentioned."

6. Important Information
   - Mention any other important information from the meeting.

Keep the summary factual.
Do not invent information that is not present in the transcript.

Meeting Transcript:
{text}
"""

    try:

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return f"LLM Error: {str(e)}"


# ---------------------------------------------------------
# STREAMLIT UI
# ---------------------------------------------------------

st.markdown(
    "<div class='main-title'>🎙️ Meeting Summarizer</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>Speech to Text + LLM Meeting Summary</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<br>",
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# COLUMNS
# ---------------------------------------------------------

c1, c2 = st.columns(2)


# ---------------------------------------------------------
# AUDIO UPLOAD
# ---------------------------------------------------------

with c1:

    st.subheader("Upload Meeting Audio")

    uploaded_file = st.file_uploader(
        "Upload an audio file",
        type=[
            "wav",
            "mp3",
            "m4a",
            "webm",
            "ogg",
            "flac"
        ]
    )


# ---------------------------------------------------------
# PROCESS BUTTON
# ---------------------------------------------------------

with c2:

    st.subheader("Process Meeting")

    process_button = st.button(
        "Transcribe & Summarize",
        type="primary",
        use_container_width=True
    )


# ---------------------------------------------------------
# MAIN PROCESSING
# ---------------------------------------------------------

if process_button:

    if uploaded_file is None:

        st.warning(
            "Please upload a meeting audio file first."
        )

    else:

        # ---------------------------------------------
        # SPEECH TO TEXT
        # ---------------------------------------------

        text = transcriber(uploaded_file)

        if text != "error" and text.strip():

            # -----------------------------------------
            # LLM SUMMARY
            # -----------------------------------------

            with st.spinner(
                "Generating meeting summary..."
            ):

                summary = llm_summary(text)

            # -----------------------------------------
            # DISPLAY SUMMARY
            # -----------------------------------------

            st.divider()

            st.header("Meeting Summary")

            st.markdown(summary)

            # -----------------------------------------
            # DOWNLOAD SUMMARY
            # -----------------------------------------

            st.download_button(
                label="Download Summary",
                data=summary,
                file_name="meeting_summary.txt",
                mime="text/plain"
            )

            # -----------------------------------------
            # DISPLAY TRANSCRIBED TEXT
            # -----------------------------------------

            st.divider()

            st.header("Transcribed Text")

            st.text_area(
                "Speech-to-Text Output",
                value=text,
                height=300
            )

            # -----------------------------------------
            # DOWNLOAD TRANSCRIPT
            # -----------------------------------------

            st.download_button(
                label="Download Transcript",
                data=text,
                file_name="meeting_transcript.txt",
                mime="text/plain"
            )

        else:

            st.error(
                "No valid text could be extracted from the audio."
            )