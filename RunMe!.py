import time
import pyautogui
import random
import string
s = 0
ascii_simvollari = [chr(i) for i in range(32, 127)]
def kombinasiya(uzunluq):
    
    simvollar = ascii_simvollari.copy()
    siyahi = ''
    for i in range(uzunluq):
        if len(simvollar) == 0:
            uzunluq *= 2
            simvollar = ascii_simvollari.copy()
        simvol = random.choice(simvollar)
        siyahi += simvol
        simvollar.remove(simvol)
    return siyahi

def bot():
    time.sleep(8)
    text = open('msg.txt')
    for i in text:
        r = random.randint(0,60)
        pyautogui.typewrite(i+'' + kombinasiya(3))
        pyautogui.press('enter')
    
while True:
    bot()
    s = s+1
    print('{} göndərildi'.format(s))
