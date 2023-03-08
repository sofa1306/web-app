from flask import Flask
import PySimpleGUIWeb as sg

app = Flask(__name__)    

@app.route('/')
def hello_world():    
    layout = [[sg.Text('demo')],      
                     [sg.Text("name"),sg.InputText()],
                     [sg.Text("age"),sg.InputText()],
                     [sg.Text("tall"),sg.InputText()],
                     [sg.Submit(), sg.Cancel()]]      

    window = sg.Window('Window Title', layout)    

    event, values = window.read()    
    window.close()

    text_input = values[0], values[1], values[2]
    sg.popup('Your info', text_input)
