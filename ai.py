import os
import pyttsx3
import pyaudio as py
import speech_recognition as sr
from openai import OpenAI



client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="Your API key",
)

def chat_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()


def speak(text):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-10)
    engine.say(text)
    engine.runAndWait()






def capture_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        text = ""
        print("Sorry, I didn't understand that.")
    except sr.RequestError as e:
        text = ""
        print("Error; {0}".format(e))
    return text


# def call(name):
#     import time
#     import pyautogui
#     os.system(f"open -a FaceTime 'tel://{name}'")
#     pyautogui.click(x=1367, y=45, clicks=1, interval=4, button='left')
#     time.sleep(1)
#     pyautogui.click(x=1367, y=45, clicks=1, interval=4, button='left')





while(1):
    inp=capture_voice_input()



    if "bye" in inp:
        break

    elif inp=="":
        continue
    else:
        out = chat_gpt(inp)
        out.replace("'","")
        print("Assi : ",f'{out}')
        speak(f'{out}')

   

