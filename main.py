import os
from os import sys
import speech_recognition as sr
from selenium import webdriver

browser = None
system_on = True

def tts(message):
    if sys.platform == 'darwin':
        tts_command = 'say'
        print(message)
        return os.system(tts_command + ' ' + message)

def execute(command):
    if command  == 'open firefox and go to google':
        tts('Opening Firefox browser')
        global browser
        browser = webdriver.Firefox()
        browser.maximize_window()
        browser.get('https://www.google.com')
    elif command == 'close firefox':
        tts('Closing Firefox browser')
        browser.quit()
    elif command == 'tell me about yourself':
        tts('I am a simple Virtual Assistant AI created by Christian Choi')
    elif command == 'goodbye':
        global system_on
        system_on = False
    else:
        tts('Sorry, I dont know what that means')

def prompt():
    with source:
        tts('What is your command?')
        answer = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(answer)
        print('What was heard: ' + command)
        #command = recognizer.recognize_google(recognizer.listen(source))
        execute(command.lower())
    except sr.UnknownValueError:
        print('What you said was not interpreted by the system.')
    except sr.RequestError as e:
        print('Request error')

tts('Welcome! I am a Virtual Assistant.')

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    # print("What is your name?")
    tts('What is your name?')
    response = recognizer.listen(source)

try:
    print('What was heard: ' + recognizer.recognize_google(response))
    words = recognizer.recognize_google(response)
    tts('Hello ' + words + '! Nice to meet you!')
except sr.UnknownValueError:
    print('What you said was not interpreted by the system.')
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

while system_on:
    prompt()

tts('Have a nice day. Goodbye!')
