import pyttsx3



def vocal_rate(engine, mult):
    wpm = 200 * mult
    engine.setProperty('rate', wpm)

def run_vocals(engine, mytext):
    engine.say(mytext)
    engine.runAndWait()
