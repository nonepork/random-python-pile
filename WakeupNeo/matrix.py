# idea from https://www.youtube.com/watch?v=gMBqciJJxqc
from os import system
from string import ascii_letters, punctuation
from time import sleep

green_text = "\033[92m"

target = "Wake up, Neo...\nThe Matrix has you...\nFollow the white rabbit.\n\nKnock, Knock, Neo."

ttp = "                                                                                  "
index = 0
character_list = ascii_letters + punctuation

for e in target:
    if(e==' '):
        index+=1
        continue
    elif (e=='\n'):
        t = list(ttp)
        t[index] = '\n'
        ttp = "".join(t)
        index+=1
        continue
    for x in character_list:
        t = list(ttp)
        t[index] = x
        ttp = "".join(t)
        ttx = f"{green_text}{ttp}"
        sleep(0.02)

        print("\033c", end="")
        print(ttx)
        if(e == x):
            index+=1
            break

system("curl ascii.live/knot")
