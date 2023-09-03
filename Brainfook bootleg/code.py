# -*- coding: utf-8 -*-

from tkinter import filedialog
import os
import time

# https://ctflearn.com/challenge/1050

array = [0]

help = """
 Language is based on stack (works somewhat like an array)
 Initially stack consists of one element, which value is 0

 "-" decreases stack's last element's value by 1
 "+" increases stack's last element's value by 1
 ">" puts first element at the end of the stack and shifts every other down
 "<" puts last element at the beginning of the stack and shifts every other up
 "@" exchanges last 2 elements
 "." duplicates stack's last element and puts it at the end of the stack
 "€" write every stack's element's value in ASCII into output.txt
 "$" open txt file and read command in it
 "c" clear terminal text
 "? or h" help command
"""

def check_command(command):
    if len(command) > 1:
        for i in command:
            check_command(i)
    elif command == "h" or command == "?":
        print(help)
    elif command == "-":
        array[-1] -= 1
    elif command == "+":
        array[-1] += 1
    elif command == ">":
        temp = array[0]
        array.pop(0)
        array.append(temp)
    elif command == "<":
        temp = array[-1]
        array.pop(-1)
        array.insert(0, temp)
    elif command == "@":
        array[-1], array[-2] = array[-2], array[-1]
    elif command == ".":
        array.append(array[-1])
    elif command == "c":
        os.system("cls")
    elif command == "$": # Open file and read command"
        file_path = filedialog.askopenfilename()
        with open(file_path, "r") as f:
            commands = f.readline()
        for i in commands:
            check_command(i)
    elif command == "€":
        with open("output.txt", "a", encoding="utf-8") as f:
            for i in array:
                f.write(chr(i))
    else:
        print("Invalid input!, continue after 10 seconds")
        time.sleep(10)

while True:
    command = str(input(""))
    check_command(command)
    print(array)
