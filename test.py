import keyboard

def here():
    print('a')


keyboard.on_press_key('f', here)
while True:
    pass
