import os
from modules import PySimpleGUI as sg


def main():
    runners = os.listdir(os.getenv("HOME") + "/.local/share/lutris/runners/wine")
    sg.theme("Tan")
    logo = [
        [sg.Image("gfx/logo.png"), sg.Text("LutriGEN", font=("Helvetica", 22))]
    ]
    name = [
        [sg.Text("Insert Game or Application name:")],
        [sg.Input(key="-APP-")]
    ]
    wine_runner = [
        [sg.Text("Select Wine/Proton runner:")],
        [sg.Combo(runners)]
    ]
    arch = [
        [sg.Text("Select architecture:")],
        [sg.Radio("Win32", "1"), sg.Radio("Win64", "1")]
    ]
    method = [
        [sg.Text("Choose installation method:")],
        [sg.Radio("executable file", "2"), sg.Radio("CD/DVD/ISO file", "2")]
    ]
    run_lutris = [
        [sg.Button("Install Game or Application")]
    ]
    layout = [
        [sg.Column(logo)],
        [sg.Column(name)],
        [sg.Column(wine_runner)],
        [sg.Column(arch)],
        [sg.Column(method)],
        [sg.Column(run_lutris)]
    ]
    window = sg.Window("LutriGEN", layout)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
    window.close()

main()