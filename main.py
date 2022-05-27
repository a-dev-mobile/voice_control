import os
import subprocess
from turtle import listen
import speech_recognition

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5

command_dict = {'commands': {
    'greeting': ['почта', 'открой почту', 'почту', ]}}


def listen_command():

    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)

            query = sr.recognize_google(
                audio_data=audio, language='ru-RU').lower()
            print("Said >>> "+ query)
            return query
    except speech_recognition.UnknownValueError:
        return '!!! Voice command error !!!'


def greeting():
    current_dir = "c:/trofimov/APP/ThunderbirdPortable/"
    p = subprocess.Popen(os.path.join(
        current_dir, "ThunderbirdPortable.exe"), cwd=current_dir)
    return 'Welcome to the Google  '


def main():
    query = listen_command()

    for k, v in command_dict['commands'].items():
        if query in v:
            print(globals()[k]())


if __name__ == '__main__':
    main()
