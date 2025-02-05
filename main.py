import tkinter as tk
from tkinter import messagebox
import maliang,os,json
from simpleeval import simple_eval
script_dir = os.path.abspath(__file__)
script_dir = os.path.dirname(script_dir)
def testread():
    global i
    try:
        with open(script_dir + "\settingjsq.json",'r') as f:
            i = json.load(f)
            return i
    except FileNotFoundError:
        messagebox.showerror("错误","未找到配置文件，请恢复配置文件")
    except json.decoder.JSONDecodeError:
        messagebox.showerror("错误","配置文件格式错误，请恢复配置文件")
    except:
        messagebox.showerror("错误","未知错误，请重新安装软件或提交Issue")
config = testread()
if config["AutoAddDY"] == "True":
    Json_AddDy_molily = True
else:
    Json_AddDy_molily = False
if config["AutoDelDY"] == "True":
    Json_DelDy_molily = True
else:
    Json_DelDy_molily = False
window = maliang.Tk(title="计算器")
window.alpha(config["BTMd"])
window.center()
window.iconbitmap(os.path.join(script_dir, 'logojsq.ico'))
canvas = maliang.Canvas(window, zoom_item=True, keep_ratio="min", free_anchor=True)
canvas.place(width=1280, height=720, x=640, y=360, anchor="center")
maliang.Text(canvas, (700, 200), text="计 算 器", fontsize=48, anchor="center")
maliang.Text(canvas, (600, 240), text="算式", anchor="nw")
entry = maliang.InputBox(canvas,position=(600,270))
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
            messagebox.showinfo("结果",str(var) + "=" + str(simple_eval(var)))
        else:
            messagebox.showinfo("结果",eval(var))
    except:
        messagebox.showerror("错误","算式错误")
    del var
def setting():
    global Json_AddDy_molily,Json_DelDy_molily,i,icon_path
    tl = maliang.Toplevel(window,title="计算器")
    window.alpha(config["BTMd"])
    window.iconbitmap(os.path.join(script_dir, 'logojsq.ico'))
    canvas = maliang.Canvas(tl, zoom_item=True, keep_ratio="min", free_anchor=True)
    canvas.place(width=1280, height=720, x=640, y=360, anchor="center")
    maliang.Text(canvas, (20, 10), text="自动将输出的结果加上算式", anchor="nw")
    maliang.Switch(canvas, (20, 40), command=orca,default=Json_AddDy_molily)
    maliang.Text(canvas, (280, 10), text="自动将输入的结果删除=", anchor="nw")
    maliang.Switch(canvas, (280, 40), command=ordd,default=Json_DelDy_molily)
    maliang.Text(canvas, (20, 80),text=("不透明度"))
    maliang.Slider(canvas, (20, 100), default=config["BTMd"], command=btms)
    maliang.Text(canvas, (20, 130),text=i["BTMd"])
    maliang.Button(canvas, text="保存设置",position=(150, 140),command=save_setting)
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
def btms(b):
    global f,i,script_dir
    if b < 0.4:
        messagebox.showinfo("禁止操作","不透明度不能小于0.4")
    try:
        with open(script_dir+"\settingjsq.json",'r') as f:
            i = json.load(f)
            i["BTMd"] = b

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
button = maliang.Button(canvas,text='计算',command=change_state,position=(600,320))
button = maliang.Button(canvas,text='设置',command=setting,position=(600,370))
window.mainloop()
