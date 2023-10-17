import PySimpleGUI as sg

sg.theme("Dark Grey 13")

# ウィンドウに配置するコンポーネント
layout = [  [sg.Text("タイピングする問題を入力してください"), sg.InputText()],
            [sg.Button("search", key=("-SEARCH-")), sg.Button("start", key=("-START-"))],
            [sg.Output(size=(80, 10), key=("-LOG-"))],
            [sg.Text('input'),sg.In(size=(30, 30), key='-IN-')],
            [sg.Button("exit"), sg.Button("clear", key="-CLEAR-")]
]

# ウィンドウの生成
window = sg.Window("typing", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    elif event == "-SEARCH-":
        print(12)
    elif event == "-START-":
        aaa = 1
    elif event == "-CLEAR-":
        # -OUTPUT-」領域を、空白で更新します。
        window["-LOG-"].update("")

window.close()
