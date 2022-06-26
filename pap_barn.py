import tkinter as tk
import random

root = tk.Tk()
canvas = tk.Canvas(root, bg="black", height=600, width=600)
canvas.pack()


f1 = {'a': 0, 'b': 0, 'c': 0, 'd': 0.16, 'e': 0, 'f': 0}
f2 = {'a': 0.85, 'b': 0.04, 'c': -0.04, 'd': 0.85, 'e': 0, 'f': 1.6}
f3 = {'a': 0.2, 'b': -0.26, 'c': 0.23, 'd': 0.22, 'e': 0, 'f': 1.6}
f4 = {'a': -0.15, 'b': 0.28, 'c': 0.26, 'd': 0.24, 'e': 0, 'f': 0.44}

x, y = 0, 0
pp = (0, 0)

def dots():
    global f1, f2, f3, f4, x, y, pp
    r = random.random()
    if r <= 0.01:
        x, y = 0, f1['d'] * pp[1]
    elif r <= 0.86:
        x, y = f2['a'] * pp[0] + f2['b'] * pp[1], f2['c'] * pp[0] + f2['d'] * pp[1] + f2['f']
    elif r <= 0.93:
        x, y = f3['a'] * pp[0] + f3['b'] * pp[1], f3['c'] * pp[0] + f3['d'] * pp[1] + f3['f']
    else:
        x, y = f4['a'] * pp[0] + f4['b'] * pp[1], f4['c'] * pp[0] + f4['d'] * pp[1] + f4['f']
    pp = (x, y)
    #print(pp)
    canvas.create_line(pp[0]*60 + 300, 600 - (pp[1]*60), pp[0]*60 + 301, 600 - (pp[1]*60), fill='green')
    root.after(1, dots)

root.after(0, dots)
root.mainloop()