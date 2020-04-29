import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio_data = r.listen(source)
    print("Recognizing.......")
    text=r.recognize_google(audio_data,language="hi-IN")
    print(text)
    print(r.recognize_google(audio_data))
