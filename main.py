import tkinter as tk
from tkinter import messagebox
import tkintertools,os,json
script_dir = os.path.abspath(__file__)
script_dir = os.path.dirname(script_dir)
window = tkintertools.Tk(title="计算器")
window.alpha(0.995)
window.center()
window.iconbitmap(os.path.join(script_dir, 'logojsq.ico'))
canvas = tkintertools.Canvas(window, zoom_item=True, keep_ratio="min", free_anchor=True)
canvas.place(width=1280, height=720, x=640, y=360, anchor="center")
tkintertools.Text(canvas, (700, 200), text="计 算 器", fontsize=48, anchor="center")
tkintertools.Text(canvas, (600, 240), text="算式", anchor="nw")
entry = tkintertools.InputBox(canvas,position=(600,270))
def testread():
    i = None
    try:
        with open(script_dir+"\settingjsq.json",'r') as f:
            i = json.load(f)
    except FileNotFoundError:
        messagebox.showerror("错误","未找到配置文件，请恢复配置文件")
    except json.decoder.JSONDecodeError:
        messagebox.showerror("错误","配置文件格式错误，请恢复配置文件")
    except:
        messagebox.showerror("错误","未知错误，请重新安装软件或提交Issue")
    return i
config = testread()
if config["AutoAddDY"] == "True":
    Json_AddDy_molily = True
else:
    Json_AddDy_molily = False
if config["AutoDelDY"] == "True":
    Json_DelDy_molily = True
else:
    Json_DelDy_molily = False
def change_state():
    global Json_AddDy_molily
    if Json_DelDy_molily == True:
        var = entry.get()
        if "=" in list(var):
            var = var.replace("=","",1)
    else:
        var = entry.get()
    try:
        if Json_AddDy_molily == True:
            messagebox.showinfo("结果",str(var)+str(eval(var)))
        else:
            messagebox.showinfo("结果",eval(var))
    except:
        messagebox.showerror("错误","算式错误")
    del var
def setting():
    global icon_path
    tl = tkintertools.Toplevel(window,title="计算器")
    window.alpha(0.995)
    window.iconbitmap(os.path.join(script_dir, 'logojsq.ico'))
    canvas = tkintertools.Canvas(tl, zoom_item=True, keep_ratio="min", free_anchor=True)
    canvas.place(width=1280, height=720, x=640, y=360, anchor="center")
    tkintertools.Text(canvas, (20, 10), text="自动将输出的结果加上算式", anchor="nw")
    tkintertools.Switch(canvas, (20, 40), command=orca,default=Json_AddDy_molily)
    tkintertools.Text(canvas, (280, 10), text="自动将输入的结果删除=", anchor="nw")
    tkintertools.Switch(canvas, (280, 40), command=ordd,default=Json_DelDy_molily)
    tkintertools.Button(canvas, text="保存设置",position=(150, 80),command=save_setting)
    tl.mainloop()
def orca(a):
    global f,i,script_dir
    try:
        with open(script_dir+"\settingjsq.json",'r') as f:
            i = json.load(f)
            if i["AutoAddDY"] == "True":
                i["AutoAddDY"] = "False"
            else:
                i["AutoAddDY"] = "True"

    except FileNotFoundError:
        messagebox.showerror("错误","未找到配置文件，请恢复配置文件")
    except json.decoder.JSONDecodeError:
        messagebox.showerror("错误","配置文件格式错误，请恢复配置文件")
    except:
        messagebox.showerror("错误","未知错误，请重新安装软件")
def ordd(a):
    global f,i,script_dir
    try:
        with open(script_dir+"\settingjsq.json",'r') as f:
            i = json.load(f)
            if i["AutoDelDY"] == "True":
                i["AutoDelDY"] = "False"
            else:
                i["AutoDelDY"] = "True"

    except FileNotFoundError:
        messagebox.showerror("错误","未找到配置文件，请恢复配置文件")
    except json.decoder.JSONDecodeError:
        messagebox.showerror("错误","配置文件格式错误，请恢复配置文件")
    except:
        messagebox.showerror("错误","未知错误，请重新安装软件")
def save_setting():
    global f,i
    with open(script_dir+"\settingjsq.json",'w') as f:
        json.dump(i,f,indent=4)
    testread()
button = tkintertools.Button(canvas,text='计算',command=change_state,position=(600,320))
button = tkintertools.Button(canvas,text='设置',command=setting,position=(600,370))
window.mainloop()
