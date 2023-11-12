from .abstract_ai_gui_shared import *
import os
from abstract_utilities import HistoryManager,write_to_file
import re
import math
from functools import reduce
from ..gpt_classes.prompt_selection import (num_tokens_from_string,
                                            chunk_any_to_tokens,
                                            get_code_blocks)
def find_common_denominator(indent_lists):
    # Flatten the list of lists and remove zeros
    all_indents = [indent for sublist in indent_lists for indent in sublist if indent != 0]

    # Find GCD of all indentation levels
    if all_indents:
        return reduce(math.gcd, all_indents)
    else:
        return 1  # Return 1 if there are no indentations other than 0
def infer_tab_size(file_path):
    if not os.path.isfile(file_path):
        write_to_file(file_path=file_path,contents='\t')
    with open(file_path, 'r') as file:
        for line in file:
            if '\t' in line:
                # Assuming the first tab character aligns with a known indentation level
                return len(line) - len(line.lstrip())  # The length of indentation
    return 4  # Default if no tab found
def get_blocks(data, delim='\n'):
    if isinstance(data, list):
        return data, None
    if isinstance(data,tuple):
        data,delim=data[0],data[-1]
    if isinstance(data, list):
        return data, delim
    return data.split(delim), delim
def get_indent_levels(text,window):
    tab_size,indent_list = infer_tab_size('config.txt'),[0]
    window['IndentSlider'].tick_interval=4
    for line in text.split('\n'):
        indent = 0
        for char in line:
            if char in [' ','\t']:
                if char == ' ':
                    indent+=1
                else:
                    indent +=tab_size
            else:
                break
    if indent not in indent_list:
        indent_list.append(indent)
    return indent_list
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
    def drop_downs_component(self, key):
        layout = []
        
        
        # DATA tab
        data_tab_content = make_component("Multiline",
                                          key=key,
                                          enable_events=True,
                                          right_click_menu=right_click_menu,
                                          **expandable())
        layout.append(make_component("Tab", "DATA", [data_tab_content]))  # Removed extra list nesting

        # PARSED tab
        parsed_key = text_to_key(key, section='PARSED')
        parsed_tab_content = make_component("Multiline",
                                            key=parsed_key,
                                            enable_events=True,
                                            right_click_menu=right_click_menu,
                                            **expandable())
        layout.append(make_component("Tab", "PARSED", [parsed_tab_content]))  # Removed extra list nesting

        return make_component("TabGroup", layout, **expandable())
    def return_multiline_scale(self, key, section=''):
        
        self.history_mgr.add_history_name(key)
        layout = []

        layout.append(make_component("Combo",
                                      values=[],
                                      key=text_to_key('delim', section=key),
                                      enable_events=True,
                                      size=(5, 1)))
        layout.append([make_component("Slider",
                                      resolution=None,
                                      orientation='horizontal',
                                      range=(0, 10),
                                      set_to_index=0,
                                      key=text_to_key('IndentSlider', section=key),
                                      tick_interval=4,
                                      enable_events=True)])
        layout.append(self.drop_downs_component(key))  # Assuming this returns a component or a list of components

        return [layout]
                
    def slice_it_up(text,window,delimiter='\n'):
       chunks = chunk_any_to_tokens(data=text,max_tokens=4022, delimiter=delimiter,reverse=False)
       slices = len(chunks)
       tokens = []
       for each in chunks:
           tokens.append(num_tokens_from_string(each))
       window['parsed'].update(value=chunks)
    # Create the window
    
    def right_click_event(self,values,event,window):
        if self.script_event_js['event'] in keys:
            multi_text = values[self.script_event_js['event']]
            indent_levels = get_indent_levels(multi_text,window)
            if indent_levels:
                window['IndentSlider'].update(range=(min(indent_levels), max(indent_levels)))
            Values = extract_unique_characters(multi_text)
            # Update combo values based on unique characters
            if Values:
                window[self.script_event_js['delim']].update(values=Values, value=Values[0])
            else:
                window[self.script_event_js['delim']].update(values=default_combo_values)
            slice_it_up(multi_text, window)
            
        elif self.script_event_js['found'] == 'IndentSlider':
            indent_level = int(values[self.script_event_js['IndentSlider']])
            # Ensure indent_level is in indent_levels
            if indent_levels:
                if indent_level in indent_levels:
                    blocks = get_code_blocks(multi_text, indent_level)
                    slice_it_up(blocks, window,delimiter=None)
        elif self.script_event_js['found'] == 'delim':
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
        else:
            self.history_mgr.add_to_history(self.key, values[self.key])

