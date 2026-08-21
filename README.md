# 🎙️ Meeting Summarizer

An AI-powered tool that converts raw meeting audio into a clean, structured summary — automatically. Upload a recording, and get back a well-organized breakdown of what was discussed, decided, and assigned, along with the full transcript.

## 📌 Overview

Teams record meetings all the time, but rarely go back and write proper minutes — important decisions and action items often get lost. This project solves that by combining speech-to-text transcription with an LLM-based summarization pipeline, producing meeting notes that are ready to share in seconds.

## ✨ Features

- **Audio Upload** — supports WAV, MP3, M4A, WEBM, OGG, and FLAC formats
- **Automatic Transcription** — converts speech to text using speech recognition
- **AI-Generated Summary** — structured into clear sections:
  - Overall Summary
  - Key Discussion Points
  - Decisions Made
  - Action Items (with responsible person, if mentioned)
  - Deadlines and Follow-ups
  - Important Information
- **Factual & Grounded** — prompt-engineered to avoid inventing information not present in the transcript
- **Downloadable Output** — export both the summary and the full transcript as text files
- **Clean, Modern UI** — built with Streamlit, styled with the Poppins font

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| Speech-to-Text | `speech_recognition` (Google Speech Recognition API) |
| Audio Processing | `pydub` (requires `ffmpeg` installed locally) |
| Summarization | Gemini LLM API |
| Config | `python-dotenv` |

## 🚀 How It Works

1. Upload a meeting audio file.
2. The audio is normalized (mono, 16kHz) and transcribed to text.
3. The transcript is passed to an LLM with a structured prompt.
4. The app displays the generated summary first, followed by the full transcript.
5. Download either output as a `.txt` file.

## ⚙️ Setup

```bash
# Install dependencies
pip install streamlit speech_recognition pydub python-dotenv google-genai

# Make sure ffmpeg is installed on your system (required by pydub)

# Add your API key to a .env file
echo "GEMINI_API_KEY=your_api_key_here" > .env

# Run the app
streamlit run app.py
```

## 🎥 Video Walkthrough

A short explanation and demo of the project is available here:

**[Watch the video](https://drive.google.com/file/d/1xx2V1KqspEclZEwQpNxxMHkrJega7st1/view?usp=sharing)**

*(Make sure sharing is set to "Anyone with the link can view.")*

## 📸 Screenshots




|  |  |
|---|---|
|  |  |

## 📄 License

This project is for educational/academic purposes.
