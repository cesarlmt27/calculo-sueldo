import PySimpleGUI as sg    #type: ignore
from sueldo_liquido import *
from sueldo_bruto import *

def main_win():
    layout = [
        [sg.Text("¿Qué desea calcular?", key="-PREGUNTA-")],
        [sg.Button("Sueldo líquido", key="-OPTN1-")],
        [sg.Button("Sueldo bruto", key="-OPTN2-")]
    ]
    return sg.Window('Calculadora de sueldo', layout, finalize=True)

def liquido_win():
    layout = [
        [sg.Text("Ingresar sueldo bruto", key="-BRUTO-")],
        [sg.Input(key="-INPUT1-")],
        [sg.Text(key="-OUTPUT1-", visible=False)],
        [sg.Button("Calcular", key="-BTN1-")]
    ]
    return sg.Window('Calcular sueldo líquido', layout, finalize=True)

def bruto_win():
    layout = [
        [sg.Text("Ingresar sueldo líquido", key="-LIQUIDO-")],
        [sg.Input(key="-INPUT2-")],
        [sg.Text(key="-OUTPUT2-", visible=False)],
        [sg.Button("Calcular", key="-BTN2-")]
    ]
    return sg.Window('Calcular sueldo bruto', layout, finalize=True)

window1 = main_win()
window2 = None
window3 = None

while True:
    window, event, values = sg.read_all_windows()

    if event == sg.WINDOW_CLOSED:
        window.close()
        if window == window2:
            window2 = None
        elif window == window3:
            window3 = None
        elif window == window1:
            break
    elif event == "-OPTN1-":
        window2 = liquido_win()
    elif event == "-OPTN2-":
        window2 = bruto_win()
    elif event == "-BTN1-":
        print(values["-INPUT1-"])
        window["-OUTPUT1-"].update("Sueldo líquido: " + values["-INPUT1-"], visible=True)
    elif event == "-BTN2-":
        print(values["-INPUT2-"])
        window["-OUTPUT2-"].update("Sueldo bruto: " + values["-INPUT2-"], visible=True)

window.close()