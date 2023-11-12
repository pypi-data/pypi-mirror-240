class AbstractNavigationManager:
    def __init__(self,selfs,window_mgr):
        self.window_mgr = window_mgr
        self.selfs =selfs
    
    def chunk_event_check(self):
        """
        Checks if any events related to the chunk UI elements were triggered and performs the necessary actions.
        """
        # Simplified method to determine the type and direction of navigation
        navigation_type, navigation_direction = self.parse_navigation_event(self.event)

        # Early exit if the event is not a navigation event
        if not navigation_type:
            return

        # Retrieve navigation data based on the event
        nav_data = self.get_navigation_data(navigation_type)

        # Update the section and subsection numbers based on navigation
        self.update_navigation_counters(nav_data, navigation_direction)

        # Update the display based on the updated navigation data
        self.update_display(nav_data)

    def parse_navigation_event(self, event):
        """
        Parses the event to extract navigation type and direction.
        """
        if event.startswith('-') and event.endswith('-'):
            parts = event[1:-1].lower().split('_')
            if 'back' in parts or 'forward' in parts:
                nav_type = '_'.join(parts[:-2]) if 'section' in parts else parts[0]
                nav_direction = parts[-1]
                return nav_type, nav_direction
        return None, None

    def get_navigation_data(self, navigation_type):
        """
        Retrieves the necessary data for navigation based on the navigation type.
        """
        nav_data = {
            'data_type': navigation_type,
            'section_number': int(self.window_mgr.get_from_value(f"-{navigation_type.upper()}_SECTION_NUMBER-")),
            'number': self.get_sub_section_number(navigation_type),
            'reference_object': self.get_reference_object(navigation_type)
        }
        return nav_data

    def get_sub_section_number(self, navigation_type):
        """
        Retrieves the current sub-section number based on navigation type.
        """
        spl = self.window_mgr.get_event().split('_')
        section = spl[1]
        self.number_key = f"-{navigation_type.upper()}{'_SECTION' if len(spl)>= 3 else ''}_NUMBER-"
        return int(self.window_mgr.get_from_value(self.number_key)) if self.window_mgr.exists(self.number_key) else None

    def get_reference_object(self, navigation_type):
        """
        Retrieves the reference object based on navigation type.
        """
        reference_js = {
            "request": self.selfs.request_data_list,
            "prompt_data": self.selfs.prompt_data_list,
            "chunk": self.selfs.prompt_mgr.chunk_token_distributions,
            "query": self.selfs.prompt_mgr.chunk_token_distributions
        }
        return reference_js.get(navigation_type, [])

    def update_navigation_counters(self, nav_data, direction):
        """
        Updates section and subsection numbers based on the navigation direction.
        """
        def get_adjusted_number(current_number, reference_obj):
            return max(0, min(current_number, max(0, len(reference_obj))))
        reference_obj = nav_data['reference_object']
        current_section_number = self.selfs.display_number_tracker['prompt_data']
        current_section_number = get_adjusted_number(current_section_number, reference_obj)
        if 'SECTION' in self.number_key:
            max_value = max(0, len(reference_obj) - 1)
            increment = 1 if direction == 'forward' else -1
            nav_data['section_number'] = max(0, min(current_section_number + increment, max_value))
            nav_data["number"]=0
        elif nav_data['data_type'] in ["chunk", "query"]:
            reference_obj = reference_obj[current_section_number]
            current_chunk_number = self.selfs.display_number_tracker['chunk_number']
            current_chunk_number = get_adjusted_number(current_chunk_number, reference_obj)

            max_value = max(0, len(reference_obj) - 1)
            increment = 1 if direction == 'forward' else -1
            nav_data['number'] = max(0, min(current_chunk_number + increment, max_value))

        self.update_display(nav_data)

    def update_display(self, nav_data):
        """
        Updates the display based on the navigation data.
        """
        self.selfs.display_number_tracker['prompt_data']=nav_data["section_number"]
        self.selfs.display_number_tracker['request']=nav_data["section_number"]
        self.selfs.display_number_tracker['query']=nav_data["section_number"]
        self.selfs.display_number_tracker['chunk']=nav_data["section_number"]
        self.selfs.display_number_tracker['chunk_number']=nav_data["number"]
        
        self.window_mgr.update_value(key=text_to_key("prompt_data section number"),value=nav_data["section_number"])
        self.window_mgr.update_value(key=text_to_key("request section number"),value=nav_data["section_number"])
        self.selfs.update_request_data_display(nav_data["section_number"])
        self.selfs.update_prompt_data_display(nav_data["section_number"])

        self.window_mgr.update_value('-CHUNK_SECTION_NUMBER-',nav_data['section_number'])
        self.window_mgr.update_value('-QUERY_SECTION_NUMBER-',nav_data['section_number'])
        self.window_mgr.update_value("-CHUNK_SECTIONED_DATA-",self.selfs.prompt_mgr.chunk_token_distributions[nav_data["section_number"]][0]['chunk']['data'])
        self.window_mgr.update_value(key='-QUERY-',value=self.selfs.prompt_mgr.create_prompt(chunk_token_distribution_number=nav_data['section_number'],chunk_number=0))
        self.window_mgr.update_value('-QUERY_NUMBER-',nav_data["number"])
        self.window_mgr.update_value('-CHUNK_NUMBER-',nav_data["number"])
        
        self.selfs.update_chunk_info(nav_data['section_number'],nav_data["number"])
