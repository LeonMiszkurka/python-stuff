import tkinter as tk
import time as t
from math import *

def evaluate(event):
    input = entry.get()
    secret_value = "execute virus"
    if (input == secret_value):
        countdown = 9
        print("loading...virus.runtime")
        print("loading")
        print("laoding_runtime-x/bool")

        t.sleep(1)
        for x in range(countdown, 0, -1):
            print(str(x) + "...")
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