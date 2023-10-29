import pandas as pd
import PySimpleGUI as sg
import event_summary as et_sy

sg.theme("Dark Grey 13")

layout = [  [sg.Text("タイピングする問題を入力してください"), sg.InputText(default_text="question")],
            [sg.Button("search", key=("-SEARCH-")), sg.Button("start", key=("-START-"))],
            [sg.Output(size=(80, 10), key=("-LOG-"))],
            [sg.Text('入力欄'), sg.In(size=(30, 30), key="-INPUT-"), sg.Button("judgement", key=("-JUDGEMENT-")), 
             sg.Text("判定"), sg.In(size=(30, 30), key="result")],
            [sg.Button("exit"), sg.Button("clear", key="-CLEAR-")]
]

window = sg.Window("typing", layout)
# 配列の初期値設定
i = 0
k = 0
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    elif event == "-SEARCH-":
        list = et_sy.open_csv(values[0])
        print(list[i][k])
    elif event == "-JUDGEMENT-":
        output = values["-INPUT-"]
        et_sy.event_judgement(list[i][k], output)
    elif event == "-START-":
        aaa = 1
    elif event == "-CLEAR-":
        window["-LOG-"].update("")

window.close()
