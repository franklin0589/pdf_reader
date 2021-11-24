import file_parser as fp
import tts
import keyboard
import os

def main():
    ##parse the file
    inputs = fp.request_input()
    text = fp.parse_pdf(inputs)
    text_array = fp.split_text(text)
    pause = False;

    engine = tts.pyttsx3.init()
    clear = lambda: os.system('clear')
    speed = 1
    for line in text_array:
        if keyboard.is_pressed("Esc"):
            break

        if keyboard.is_pressed("p"):
            print("Pause"+" "*20, end = "\r")
            pause = True
        if keyboard.is_pressed("f"):
            speed+=0.1
            tts.vocal_rate(engine, 1)
        if keyboard.is_pressed("g"):
            speed-=0.1
            tts.vocal_rate(engine, speed)
        print(line+" "*20, end = "\r")
        tts.run_vocals(engine,line)

        if pause:
            keyboard.wait('q')
            pause = False







if __name__ == '__main__':
    main()
