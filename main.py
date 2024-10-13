import tkinter as tk
from tkinter import messagebox
import tkintertools,os
script_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(script_dir, 'logojsq.ico')
window = tkintertools.Tk(title="计算器")
window.alpha(0.995)
window.center()
window.iconbitmap(icon_path)
canvas = tkintertools.Canvas(window, zoom_item=True, keep_ratio="min", free_anchor=True)
canvas.place(width=1280, height=720, x=640, y=360, anchor="center")
tkintertools.Text(canvas, (700, 200), text="计 算 器", fontsize=48, anchor="center")
entry = tkintertools.InputBox(canvas,position=(600,250))
def change_state():
    var = entry.get()
    try:
        messagebox.showinfo("结果",(eval(var)))
    except:
        messagebox.showerror("错误","算式错误")
button = tkintertools.Button(canvas,text='计算',command=change_state,position=(600,300))
window.mainloop()
