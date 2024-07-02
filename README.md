# Voice Assistant with OpenAI GPT-3.5

This project is a voice assistant that uses OpenAI's GPT-3.5 model to generate responses based on user input. The assistant captures voice input, processes it, and responds using text-to-speech. 
It integrates several components: speech recognition, text-to-speech, and interaction with the OpenAI API.

## Features

- **Speech Recognition**: Captures voice input from the user.
- **OpenAI GPT-3.5 Integration**: Generates responses using OpenAI's GPT-3.5 model.
- **Text-to-Speech**: Converts text responses to speech and plays them back to the user.
- **Continuous Listening**: Listens for commands continuously until the user says "bye".

## Requirements

- Python 3.x
- OpenAI API Key
- The following Python packages:
  - `openai`
  - `pyttsx3`
  - `pyaudio`
  - `SpeechRecognition`

**Code Overview**

chat_gpt(prompt): Sends a prompt to the OpenAI API and returns the response.
speak(text): Converts text to speech and plays it back to the user.
capture_voice_input(): Captures voice input from the user using the microphone.
The main loop listens for user input continuously and processes it using the above functions.
