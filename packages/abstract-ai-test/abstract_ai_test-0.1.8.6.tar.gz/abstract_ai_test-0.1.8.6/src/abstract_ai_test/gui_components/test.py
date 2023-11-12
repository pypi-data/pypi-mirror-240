from abstract_ai.gui_components.abstract_ai_gui import get_total_layout
from abstract_gui import AbstractWindowManager

class YourClassName:  # Replace with your actual class name
    def __init__(self):
        self.window_mgr=AbstractWindowManager()
        self.window_name = self.window_mgr.add_window(window_name="Chat GPT Console",title="Chat GPT Console",layout=get_total_layout())
        self.window_mgr.set_current_window(self.window_name)
        self.window = self.window_mgr.get_window_method(self.window_name)
        self.window_mgr.while_window(window_name=self.window_name, event_handlers=self.chunk_event_check)
    
    def chunk_event_check(self,*args):
        """
        Checks if any events related to the chunk UI elements were triggered and performs the necessary actions.
        """
        self.event,self.values,self.window=args
        print(self.event)
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
        key = f"-{navigation_type.upper()}_NUMBER-"
        return int(self.window_mgr.get_from_value(key)) if self.window_mgr.exists(key) else None

    def get_reference_object(self, navigation_type):
        """
        Retrieves the reference object based on navigation type.
        """
        reference_js = {
            "request": self.request_data_list,
            "prompt_data": self.prompt_data_list,
            "chunk": self.prompt_mgr.chunk_token_distributions,
            "query": self.prompt_mgr.chunk_token_distributions
        }
        return reference_js.get(navigation_type, [])

    def update_navigation_counters(self, nav_data, direction):
        """
        Updates section and subsection numbers based on the navigation direction.
        """
        max_section = len(nav_data['reference_object']) - 1
        max_sub_section = len(nav_data['reference_object'][nav_data['section_number']]) - 1 if nav_data['number'] is not None else None

        # Update section number
        if nav_data['number'] is None:
            nav_data['section_number'] = self.calculate_new_counter(nav_data['section_number'], direction, max_section)

        # Update sub-section number
        else:
            nav_data['number'] = self.calculate_new_counter(nav_data['number'], direction, max_sub_section)

    def calculate_new_counter(self, current_counter, direction, max_value):
        """
        Calculates the new counter value based on the current value, direction, and maximum allowed value.
        """
        if direction == 'forward':
            return min(current_counter + 1, max_value)
        elif direction == 'back':
            return max(current_counter - 1, 0)
        return current_counter

    def update_display(self, nav_data):
        """
        Updates the display based on the navigation data.
        """
        # Update the display logic here based on nav_data
        pass
request_data=["""would you be so kind as to help me with this mess""",
              """hi im request 2, you may remember me from "oh my god what did i do" and "the code is not complex,
and if its complex,its neccisary, and if its not neccisary, then you dont get it, and if you get it,
welll... thanks for checking it out."""]
prompt_data = ['this is a string that needs to be chunked','string number 2 waitin ta be chonked!']
data_chunks=[
    [{'completion': {'desired': 4096, 'available': 3896, 'used': 200}, 'prompt':
      {'desired': 4096, 'available': 3702, 'used': 394}, 'chunk':
      {'number': 0, 'total': 0, 'length': 0, 'data': '#REQUEST#\n\nwould you be so kind as to help me with this mess\n\n#CHUNK DATA#\n\n1 of 1\nn\this is a string that needs to be chunked'}}],
    [{'completion': {'desired': 4096, 'available': 3896, 'used': 200}, 'prompt':
      {'desired': 4096, 'available': 3702, 'used': 394}, 'chunk':
      {'number': 0, 'total': 0, 'length': 0, 'data': '#REQUEST#\n\nhi im request 2, you may remember me from "oh my god what did i do" and "the code is not complex,and if its complex,its neccisary, and if its not neccisary, then you dont get it, and if you get it,welll... thanks for checking it out.\n\n#DATA CHUNK 1 of 1\n\nstring number 2 waitin ta be chonked!"'}}
     ]
    ]
query = {'model': 'gpt-4', 'messages': [{'role': 'assistant', 'content': '\n-----------------------------------------------------------------------------\n#instructions#\n\nyour response is expected to be in JSON format with the keys as follows:\n\n0) api_response - place response to prompt here\n1) suggestions - A parameter that allows the module to provide suggestions for improving efficiency in future prompt sequences. These suggestions will be reviewed by the user after the entire prompt sequence is fulfilled.\n2) generate_title - A parameter used for title generation of the chat. To maintain continuity, the generated title for a given sequence is shared with subsequent queries.\n\nbelow is an example of the expected json dictionary response format, with the default inputs:\n{"api_response": "", "suggestions": "", "generate_title": ""}\n-----------------------------------------------------------------------------\n#prompt#\n\ndsfdfsdsfsdfaasdf\n-----------------------------------------------------------------------------\n#REQUEST#\n\nwould you be so kind as to help me with this mess\n\n#CHUNK DATA#\n\n1 of 1\nn\this is a string that needs to be chunked'}], 'max_tokens': 3896}
def update_chunk_info(self,chunk_token_distribution_number=0,chunk_number=0):
    if self.prompt_mgr.chunk_token_distributions:
        if chunk_token_distribution_number < len(self.prompt_mgr.chunk_token_distributions) and chunk_token_distribution_number >=0:
            self.chunk_token_distribution = self.chunk_token_distributions[int(chunk_token_distribution_number)][int(chunk_number)]
            self.window_mgr.update_value(key=self.sectioned_chunk_data_key, value=self.chunk_token_distribution['chunk']['data'])
            for key in self.chunk_display_keys:
                spl = key[1:-1].lower().split('_')
                if spl[0] in self.chunk_token_distribution:
                    if spl[-1] in self.chunk_token_distribution[spl[0]]:
                        self.window_mgr.update_value(key=key,value=self.chunk_token_distribution[spl[0]][spl[-1]])
        
YourClassName()
