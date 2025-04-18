import tkinter as tk
from tkinter import messagebox
import os,json
from simpleeval import simple_eval
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
import keyboard
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton, QTextEdit, QSlider, QLabel, QMessageBox, QCheckBox, QDialog
from PyQt6.QtCore import Qt

if getattr(sys, 'frozen', False):
    script_dir = os.getcwd()
else:
    script_dir = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_dir)

def testread():
    global i
    try:
        setting_path = os.path.join(script_dir, "settingjsq.json")
        with open(setting_path, 'r') as f:
            i = json.load(f)
            return i
    except FileNotFoundError:
        messagebox.showerror("错误","未找到配置文件，请恢复配置文件")
    except json.decoder.JSONDecodeError:
        messagebox.showerror("错误","配置文件格式错误，请恢复配置文件")
    except:
        messagebox.showerror("错误","未知错误，请重新安装软件或提交Issue")

def show():
    global Json_AddDy_default
    if Json_DelDy_default == True:
        var = entry.get()
        if "=" in list(var):
            var = var.replace("=","",1)
    else:
        var = entry.get()
    try:
        if Json_AddDy_default == True:
            messagebox.showinfo("结果",str(var) + "=" + str(simple_eval(var)))
        else:
            messagebox.showinfo("结果",simple_eval(var))
    except:
        messagebox.showerror("错误","算式错误")
    del var

def orca(a):
    global f,i,script_dir
    try:
        with open(f"{script_dir}+/settingjsq.json",'r') as f:
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
        with open(f"{script_dir}+/settingjsq.json",'r') as f:
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
        with open(f"{script_dir}+/settingjsq.json",'r') as f:
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
    with open(f"{script_dir}/settingjsq.json",'w') as f:
        json.dump(i,f,indent=4)
    testread()

def askai():
    timu = str(entry.get())
    endpoint = "https://models.inference.ai.azure.com"
    model_name = "DeepSeek-R1"
    token = "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"  # os.environ["GITHUB_TOKEN"]

    client = ChatCompletionsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(token),
        connection_verify=False
    )

    response = client.complete(
        messages=[
            SystemMessage("你是一个数学老师，你需要帮助用户解决数学题，并且给出逐步思考过程，并且不要在回答中包含对你的要求，不要在回答中包含```,不要在回答中包含你的要求"),
            UserMessage("用户发来了一道数学题，它是" + timu),
        ],
        max_tokens=1000,
        model=model_name
    )

    ai_window = QDialog()
    ai_window.setWindowTitle("问AI")
    ai_window.setWindowOpacity(float(config["BTMd"]))  # 设置窗口透明度
    ai_window.setWindowIcon(QIcon(os.path.join(script_dir, 'logojsq.ico')))

    layout = QVBoxLayout()
    result_text = QTextEdit()
    result_text.setReadOnly(True)
    result_text.setText(response.choices[0].message.content)
    layout.addWidget(result_text)
    ai_window.setLayout(layout)

    ai_window.exec()


config = testread()
if config["AutoAddDY"] == "True":
    Json_AddDy_default = True
else:
    Json_AddDy_default = False
if config["AutoDelDY"] == "True":
    Json_DelDy_default = True
else:
    Json_DelDy_default = False

class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # 设置全局字体为微软雅黑
        from PyQt6.QtGui import QFont
        font = QFont("Microsoft YaHei", 10)
        QApplication.setFont(font)
        self.setWindowTitle("计算器")
        self.setGeometry(100, 100, 350, 400)  # 修改窗口尺寸

        # 主布局
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # 输入框
        self.entry = QLineEdit(self)
        self.entry.setPlaceholderText("请输入算式")
        self.entry.setFixedHeight(40)  # 增加输入框高度
        self.layout.addWidget(self.entry)

        # 计算按钮
        self.calculate_button = QPushButton("计算", self)
        self.calculate_button.setFixedHeight(40)  # 增加按钮高度
        self.calculate_button.clicked.connect(self.show_result)
        self.layout.addWidget(self.calculate_button)

        # 设置按钮
        self.setting_button = QPushButton("设置", self)
        self.setting_button.setFixedHeight(40)  # 增加按钮高度
        self.setting_button.clicked.connect(self.open_settings)
        self.layout.addWidget(self.setting_button)

        # 问AI按钮
        self.ask_ai_button = QPushButton("问AI", self)
        self.ask_ai_button.setFixedHeight(40)  # 增加按钮高度
        self.ask_ai_button.clicked.connect(self.askai)
        self.layout.addWidget(self.ask_ai_button)

        # 结果显示区域
        self.result_display = QTextEdit(self)
        self.result_display.setReadOnly(True)
        self.result_display.setFixedHeight(150)  # 调整结果显示区域高度
        self.layout.addWidget(self.result_display)

    def show_result(self):
        try:
            expression = self.entry.text()
            result = simple_eval(expression)
            self.result_display.setText(f"结果: {result}")
        except Exception as e:
            QMessageBox.warning(self, "错误", f"计算失败: {str(e)}")

    def open_settings(self):
        settings_window = SettingsWindow(self)
        settings_window.exec()

    def askai(self):
        timu = self.entry.text()
        endpoint = "https://models.inference.ai.azure.com"
        model_name = "DeepSeek-R1"
        token = "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"  # os.environ["GITHUB_TOKEN"]

        client = ChatCompletionsClient(
            endpoint=endpoint,
            credential=AzureKeyCredential(token),
            connection_verify=False
        )

        response = client.complete(
            messages=[
                SystemMessage("你是一个数学老师，你需要帮助用户解决数学题，并且给出逐步思考过程"),
                UserMessage(f"用户发来了一道数学题，它是{timu}"),
            ],
            max_tokens=1000,
            model=model_name
        )
        self.result_display.setText(response.choices[0].message.content)


class SettingsWindow(QDialog):  # 修改父类为 QDialog
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("设置")
        self.setGeometry(200, 200, 350, 300)  # 修改窗口尺寸

        layout = QVBoxLayout()

        # 自动添加算式开关
        self.add_formula_checkbox = QCheckBox("自动将输出的结果加上算式")
        self.add_formula_checkbox.setChecked(Json_AddDy_default)
        layout.addWidget(self.add_formula_checkbox)

        # 自动删除等号开关
        self.del_equal_checkbox = QCheckBox("自动将输入的结果删除=")
        self.del_equal_checkbox.setChecked(Json_DelDy_default)
        layout.addWidget(self.del_equal_checkbox)

        # 不透明度滑块
        layout.addWidget(QLabel("不透明度"))
        self.opacity_slider = QSlider(Qt.Orientation.Horizontal)
        self.opacity_slider.setMinimum(40)
        self.opacity_slider.setMaximum(100)
        self.opacity_slider.setValue(int(config["BTMd"] * 100))
        self.opacity_slider.setFixedHeight(20)  # 调整滑块高度
        layout.addWidget(self.opacity_slider)

        # 保存设置按钮
        save_button = QPushButton("保存设置")
        save_button.setFixedHeight(40)  # 增加按钮高度
        save_button.clicked.connect(self.save_settings)
        layout.addWidget(save_button)

        self.setLayout(layout)

    def save_settings(self):
        global config
        config["AutoAddDY"] = str(self.add_formula_checkbox.isChecked())
        config["AutoDelDY"] = str(self.del_equal_checkbox.isChecked())
        config["BTMd"] = self.opacity_slider.value() / 100
        save_setting()
        QMessageBox.information(self, "设置", "设置已保存")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec())
