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
#ffmpeg model is greater than 25MB. So I couldn't add these model files in the repo.

# Add your API key to a .env file
echo "GEMINI_API_KEY=your_api_key_here" > .env

# Run the app
streamlit run app.py
```

## 🎥 Video Walkthrough

A short explanation and demo of the project is available here:

**[Watch the video](https://drive.google.com/file/d/1xx2V1KqspEclZEwQpNxxMHkrJega7st1/view?usp=sharing)**

## 📸 Screenshots
<img width="1915" height="1010" alt="Screenshot 2026-08-21 125301" src="https://github.com/user-attachments/assets/1cde50c9-48f0-4813-b85e-14667976bad5" />
<img width="1919" height="1012" alt="Screenshot 2026-08-21 125406" src="https://github.com/user-attachments/assets/7be6ab45-9443-4535-b398-a4d5180fac39" />
<img width="1914" height="1016" alt="Screenshot 2026-08-21 125419" src="https://github.com/user-attachments/assets/7d37a6aa-48d6-4e8b-8a77-5a7a41a2e3d0" />
<img width="1916" height="1004" alt="Screenshot 2026-08-21 125431" src="https://github.com/user-attachments/assets/95a07963-0fcc-492f-9078-aee74d0e0789" />
<img width="1904" height="1009" alt="Screenshot 2026-08-21 125439" src="https://github.com/user-attachments/assets/cc3f83d2-cf1a-478c-85a5-2704c5f50eb8" />






|  |  |
|---|---|
|  |  |

## 📄 License

This project is for educational/academic purposes.
