import pyautogui
import time

bpm = 224

one_step = 60/bpm

with open('./1.txt', 'r') as f:
    sheet = f.read()

def half_step(line:str, fir_rest = True):
    step = one_step/2
    for n, i in enumerate(line):
        if (not n == 0) or fir_rest:
            time.sleep(step)
        pyautogui.press(i)

sheet = sheet.replace('|', ' ').replace('/', ' ').replace('\\', ' ')
sheets = sheet.split()

time.sleep(2)

for i in sheets:
    if i[0]=='[':
        i = i.split('[')
        for j in i:
            if ']' in j:
                j = j.split(']')
                pyautogui.typewrite(j[0])
                half_step(j[1])
            else:
                half_step(j, False)
    pyautogui.typewrite(i)
    time.sleep(one_step)