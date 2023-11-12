import PySimpleGUI as sg
from abstract_utilities import HistoryManager
from abstract_gui import get_event_key_js
class MultilineSlider:
    def __init__(self,history_mgr = None):
        self.keys=[]
        self.default_combo_values = []

        self.multi_text=''
        # Create an instance of HistoryManager
        self.history_mgr = history_mgr or HistoryManager()

    def get_right_click(self,key=None):
        if key != None:
            self.keys.append(key)
        return ['Right', ['Undo', 'Cut', 'Copy', 'Paste', 'Delete', 'Select All', 'Key Term Search', 'Text Parsing']]
    
    def right_click_event(self,values,event,window):
        self.script_event_js=get_event_key_js(event,self.keys)
        input(self.script_event_js)
        if self.script_event_js['found'] == 'delim':
            delim = values['delim']
            blocks = multi_text.split(delim)
            slice_it_up(blocks,window,delimiter=delim)
        elif self.script_event_js['found'] == 'Undo':
            last_data = history_manager.undo(self.key)
            window[self.script_event_js['event']].update(last_data)
        elif self.script_event_js['found'] == 'Redo':
            last_data = history_manager.redo(self.key)
            window[self.script_event_js['event']].update(last_data)      
        elif self.script_event_js['found'] ==  'Cut':
            window[self.script_event_js['event']].Widget.event_generate('<<Cut>>')
        elif self.script_event_js['found'] ==  'Copy':
            window[self.script_event_js['event']].Widget.event_generate('<<Copy>>')
        elif self.script_event_js['found'] ==  'Paste':
            window[self.script_event_js['event']].Widget.event_generate('<<Paste>>')
        elif self.script_event_js['found'] ==  'Delete':
            window[self.script_event_js['event']].Widget.event_generate('<<Clear>>')
        elif self.script_event_js['found'] ==  'Select All':
            window[self.script_event_js['event']].Widget.event_generate('<<SelectAll>>') 
        elif self.script_event_js['found'] == 'Key Term Search' or self.script_event_js['found'] == 'Text Parsing':
            drop_down_selection = event  # Do what you want with the selection    
      

# Create an instance of MultilineSlider
history_manager = HistoryManager()
multiline_slider = MultilineSlider(history_manager)

# Define the GUI layout
layout = [
    [sg.Multiline(size=(40, 10), key='-MULTI-', right_click_menu=multiline_slider.get_right_click('-MULTI-'))],
    [sg.Button('Submit')]
]

# Create the window
window = sg.Window('Multiline with Right Click', layout)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    print(event)
    
    multiline_slider.right_click_event(values, event, window)
    if event == 'Submit':
        print('Submitted Text:', values['-MULTI-'])

window.close()
