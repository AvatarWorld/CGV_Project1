print("[INFO] Intializing speech recognition and microphone, please wait.")
import speech_recognition as sr
from os import path

# obtain audio from the microphone
r = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        input("Press any key to record.")
        print("[INFO] Listening...")
        audio = r.listen(source)
        print("[INFO] audio recorded.")

    # write audio to a WAV file
    wavpath = path.join(path.dirname(path.realpath(__file__)), "microphone-result.wav")
    with open(wavpath, "wb") as f:
        f.write(audio.get_wav_data())

    """
    with sr.AudioFile('english.wav') as source:
        audio = r.record(source) # read the entire audio file
    """

    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("[INFO] Recognizing Speech.")
        transcript = r.recognize_google(audio)
        print("[SUCCESS] Google Speech Recognition thinks you said:")
        print('"'+transcript+'"')

        txtpath = path.join(path.dirname(path.realpath(__file__)), "microphone-result.txt")
        with open(txtpath, "w") as f:
            f.write(transcript)

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))