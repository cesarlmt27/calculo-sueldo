import PySimpleGUI as sg    #type: ignore
import sueldo_liquido as sl
import sueldo_bruto as sb

def main_win():
    layout = [
        [sg.Text("¿Qué desea calcular?", key="-PREGUNTA-")],
        [sg.Button("Sueldo líquido", key="-OPTN1-")],
        [sg.Button("Sueldo bruto", key="-OPTN2-")]
    ]
    return sg.Window('Calculadora de sueldo', layout, finalize=True)

def liquido_win():
    layout = [
        [sg.Text("Ingresar sueldo bruto", key="sueldo_bruto")],
        [sg.Input(key="-INPUT1-")],
        [sg.Text(key="-OUTPUT1-", visible=False)],
        [sg.Text('Tipo AFP',size=(20, 1), font='Lucida',justification='left')],
        [sg.Combo(['AFP Capital','AFP Cuprum','AFP Habitat', 'AFP Modelo','AFP Planvital','AFP Provida','AFP Uno'],default_value='AFP Capital',key='AFP')],
        [sg.Text('Tipo Contrato',size=(30, 1), font='Lucida',justification='left')],
        [sg.Combo(['Contrato indefinido','Contrato a plazo fijo'],default_value='Contrato indefinido',key='contrato')],
        [sg.Button("Calcular", key="-BTN1-")]
    ]
    return sg.Window('Calcular sueldo líquido', layout, finalize=True)

def bruto_win():
    layout = [
        [sg.Text("Ingresar sueldo liquido", key="sueldo_liquido")],
        [sg.Input(key="-INPUT2-")],
        [sg.Text(key="-OUTPUT2-", visible=False)],
        [sg.Text('Escoja su AFP',size=(20, 1), font='Lucida',justification='left')],
        [sg.Text('Tipo AFP',size=(20, 1), font='Lucida',justification='left')],
        [sg.Combo(['AFP Capital','AFP Cuprum','AFP Habitat', 'AFP Modelo','AFP Planvital','AFP Provida','AFP Uno'],default_value='AFP Capital',key='AFP')],
        [sg.Text('Tipo Contrato',size=(30, 1), font='Lucida',justification='left')],
        [sg.Combo(['Contrato indefinido','Contrato a plazo fijo'],default_value='Contrato indefinido',key='contrato')],
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
        if (sl.inputs(values["-INPUT1-"], values["AFP"],values["contrato"])) == "error":
           sg.popup("Error en los datos ingresados", "intente nuevamente ")
        else:
           sg.popup("El sueldo liquido es: ",sl.inputs(values["-INPUT1-"], values["AFP"],values["contrato"]) )     
    elif event == "-BTN2-":
        if (sb.inputs(values["-INPUT2-"], values["AFP"],values["contrato"])) == "error":
           sg.popup("Error en los datos ingresados", "intente nuevamente ")
        else:
           sg.popup("El sueldo bruto es: ",sb.inputs(values["-INPUT2-"], values["AFP"],values["contrato"]) )
window.close()