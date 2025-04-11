import keyboard
import mouse 
import time 
import pynput  # для упровление блокировкой мышки

class keyboard:
    def keyloger():
        try:
            pass
        except Exception as e:
            print("Error: ", e)

    def click(key):
        try:
            keyboard.on_press(key)
            keyboard.on_release(key)

        except Exception as e:
            print("Error:", e)

    def combinationClick(combination, key, key2, key3):
        try:
            if combination == 1:
                keyboard.on_press(key)
                keyboard.on_release(key)

            if combination == 2:
                keyboard.on_press(key, key2)
                keyboard.on_release(key, key2)
                    
            if combination == 3:
                keyboard.on_press(key, key2, key3)
                keyboard.on_release(key, key2, key3)
                
        except Exception as e:
            print("Error:", e)
    
    def blockKeyboard(timers):
        for i in range(150):
            keyboard.block_key(i)
        time.sleep(timers)

class mouse:
    def posintion():
        try:
            return mouse.get_position()
        except Exception as e:
            print("Error: ", e)

    def mouseClick(key):
        mouse.click(key)

    def mouseMove(x, y):
        x = int(x)
        y = int(y)
        mouse.move(x, y)

    def autoClicker(keyPlay, position_x, position_y, timersleeper):
        keyboard.wait(keyPlay)
        mouse.move(position_x, position_y)
        while True:
            mouse.click()
            time.sleep(timersleeper)
    
    def blockMove(timers):
        mouse_listener = pynput.mouse.Listener(suppress=True) 
        mouse_listener.start()
        time.sleep(timers)
    
    def activeMove():
        mouse_listener = pynput.mouse.Listener(suppress=True) 
        mouse_listener.stop()
