from abstract_gui import *
import json
import os

def get_response_json_info():
    data = {'id': 38, 'object': 15, 'created': 1699622029, 'model': 10, 'usage': 3, 'file_path': 144, 'title': 'Misunderstood input'}
    layout = [[]]
    file_path = []
    for key,value in data.items():
        component = make_component("Frame",str(key),ensure_nested_list(make_component('Input',value,key=text_to_key(key,section='response_output'),size=(value,1))))
        if key == 'file_path':
            file_path.append([make_component('Button',"OPEN",key='-OPEN_RESPONSE-',enable_events=True),component])
        else:
            layout[-1].append(component)
    layout.append(file_path)
    return layout

input(get_response_json_info())
