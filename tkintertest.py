import tkinter as tk
import time as t
from math import *

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

def evaluate(event):
    input = entry.get()
    secret_value = "execute virus"
    if (input == secret_value):
        countdown = 0
        print("loading...virus.runtime")
        print("loading")
        print("laoding_runtime-x/bool")

        t.sleep(1)
        for x in range(countdown, 11):
            #print(str(x) + "...")
            printProgressBar(x, 10)
            t.sleep(1)
        while (bool(1)):
            print("virus.runtime is runing")

    result_text = "Result: " + str(eval(entry.get()))
    res.configure(text=result_text)
    print("Entry: " + str(entry.get()))
    print(result_text)

w = tk.Tk()
w.geometry("500x200")
tk.Label(w, text="Your Expression:").pack()
entry = tk.Entry(w)
entry.bind("<Return>",evaluate)
entry.pack()
res = tk.Label(w)
res.pack()
w.mainloop()