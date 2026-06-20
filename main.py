# -*- coding: utf-8 -*-
import os
# 关闭彩色日志乱码
os.environ["TOGA_NO_COLOR"] = "1"
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, LEFT

def build(app):
    # 1. 先定义所有控件
    box = toga.Box(style=Pack(direction=COLUMN, margin=20))
    weight_input = toga.TextInput(placeholder="请输入你的体重(kg)", style=Pack(margin=8))
    height_input = toga.TextInput(placeholder="请输入你的身高(m)", style=Pack(margin=8))
    res_label = toga.Label(text="结果是", style=Pack(margin=10, text_align=LEFT))

    # 2. 【关键】必须先定义函数，再创建按钮
    def calculate_bmi(widget):
        try:
            w = float(weight_input.value)
            h = float(height_input.value)
            bmi = w / (h ** 2)
            if bmi < 18.5:
                res = f"BMI:{bmi:.2f}，偏瘦，需要补充营养"
            elif 18.5 <= bmi <= 25:
                res = f"BMI:{bmi:.2f}，体重正常，继续保持"
            elif 25 < bmi <= 30:
                res = f"BMI:{bmi:.2f}，轻度偏胖，注意饮食"
            else:
                res = f"BMI:{bmi:.2f}，肥胖，需要控制体重"
            res_label.text = res
        except ValueError:
            res_label.text = "错误！请输入纯数字"
        except ZeroDivisionError:
            res_label.text = "错误！身高不能填写0"

    # 3. 最后创建按钮，绑定上面已经定义好的函数
    calc_btn = toga.Button("计算BMI", on_press=calculate_bmi, style=Pack(margin=8))

    # 依次把控件放进盒子
    box.add(weight_input)
    box.add(height_input)
    box.add(calc_btn)
    box.add(res_label)
    return box

def main():
    return toga.App(formal_name="BMI计算器", app_id="com.bmi.calc", startup=build)

if __name__ == "__main__":
    app = main()
    app.main_loop()