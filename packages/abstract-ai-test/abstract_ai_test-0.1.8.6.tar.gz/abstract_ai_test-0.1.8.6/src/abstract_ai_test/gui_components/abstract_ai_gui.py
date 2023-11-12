from abstract_ai.gui_components.abstract_ai_gui_shared import *

def get_tab_layout(title,layout=None):
    if not layout:
        layout = [[make_component("Push"),make_component("Button",button_text="<-",key=text_to_key(f"{title} section back"),enable_events=True),
             make_component("input",default_text='0',key=text_to_key(f"{title} section number"),size=(4,1)),
             make_component("Button",button_text="->",key=text_to_key(f"{title} section forward"),enable_events=True),make_component("Push")],make_component("Multiline",key=text_to_key(title), **expandable())]
    return make_component("Tab",title.upper(),ensure_nested_list(layout))
def generate_tab(title, layout):
    return make_component("Tab", ensure_nested_list(layout), **expandable())
def get_prompt_tabs(layout_specs={},args={}):
    layout = []
    
    for prompt_tab_key in prompt_tab_keys:
        layout.append(get_tab_layout(prompt_tab_key,layout=layout_specs.get(prompt_tab_key)))
    return get_tab_group(layout,args=args)
def get_chunked_sections():
    return [
        [make_component("Push"),make_component("Button",button_text="<-",key=text_to_key("chunk section back"),enable_events=True),
             make_component("input",default_text='0',key=text_to_key("chunk section number"),size=(4,1)),
             make_component("Button",button_text="->",key=text_to_key("chunk section forward"),enable_events=True),make_component("Push")],
        [make_component("Push"),make_component("Button",button_text="<-",key=text_to_key("chunk back"),enable_events=True),
         make_component("input",default_text='0',key=text_to_key("chunk number"),size=(4,1)),
         make_component("Button",button_text="->",key=text_to_key("chunk forward"),enable_events=True),make_component("Push")],
        [make_component("Frame",'chunk sectioned data', layout=[[make_component("Multiline",key=text_to_key('chunk sectioned data'),enable_events=True,**expandable())]],**expandable())]]
            
def get_prompt_data_section():
    return [[make_component("Button",button_text="CREATE CHUNK",key="-CREATE_CHUNK-",auto_size_text=True, enable_events=True),
             make_component("Button",button_text="REPLACE CHUNK",key="-REPLACE_CHUNK-",auto_size_text=True, enable_events=True),
             make_component("Button",button_text="BLANK CHUNK",key="-BLANK_CHUNK-",auto_size_text=True, enable_events=True),
             make_component("Input",0,default_value=0,key="-CUSTOM_CHUNK-",auto_size_text=True, enable_events=True,size=(3,1))],
            [make_component("Push"),make_component("Button",button_text="<-",key=text_to_key("prompt_data section back"),enable_events=True),
             make_component("input",default_text='0',key=text_to_key("prompt_data section number"),size=(4,1)),
             make_component("Button",button_text="->",key=text_to_key("prompt_data section forward"),enable_events=True),make_component("Push")],
            [make_component("Frame",'prompt_data data', layout=[[make_component("Multiline",key=text_to_key('prompt_data data'),enable_events=True,**expandable())]],**expandable())]]
def get_request_section():
    return [
        [make_component("Push"),make_component("Button",button_text="<-",key=text_to_key("request section back"),enable_events=True),
             make_component("input",default_text='0',key=text_to_key("request section number"),size=(4,1)),
             make_component("Button",button_text="->",key=text_to_key("request section forward"),enable_events=True),make_component("Push")],
        [make_component("Frame",'', layout=[[make_component("Multiline",key=text_to_key('request'),enable_events=True,**expandable())]],**expandable())]]
def get_query_section():
    return [
        [make_component("Push"),make_component("Button",button_text="<-",key=text_to_key("query section back"),enable_events=True),
             make_component("input",default_text='0',key=text_to_key("query section number"),size=(4,1)),
             make_component("Button",button_text="->",key=text_to_key("query section forward"),enable_events=True),make_component("Push")],
        [make_component("Push"),make_component("Button",button_text="<-",key=text_to_key("query back"),enable_events=True),
         make_component("input",default_text='0',key=text_to_key("query number"),size=(4,1)),
         make_component("Button",button_text="->",key=text_to_key("query forward"),enable_events=True),make_component("Push")],
        [make_component("Frame",'', layout=[[make_component("Multiline",key=text_to_key('query'),**expandable())]],**expandable())]]
def get_instructions():
    layout = []
    sub_layout = []
    for instruction_key in instructions_keys:
        if instruction_key == 'instructions':
            layout.append(generate_bool_text(instruction_key, args={**expandable(size=(None, 10))}))
        else:
            component = generate_bool_text(instruction_key, args={**expandable(size=(None, 5))})
            sub_layout.append([component])
    sub_layout = [make_component("Column", ensure_nested_list(sub_layout), **expandable(size=(1600, 1600), scroll_vertical=True))]
    return [[make_component("Push"),make_component("Button",button_text="<-",key=text_to_key("instructions section back"),enable_events=True),
             make_component("input",default_text='0',key=text_to_key("instructions section number"),size=(4,1)),
             make_component("Button",button_text="->",key=text_to_key("instructions section forward"),enable_events=True),make_component("Push")],
        [make_component("Frame",'', layout=[layout, sub_layout])]]

def get_total_layout():
    prompt_tabs= get_prompt_tabs({"query":get_query_section(),"request":get_request_section(),"prompt data":get_prompt_data_section(),"instructions":get_instructions(),"chunks":get_chunked_sections()},args={**expandable(size=(int(0.4*window_width),int(window_height)))})
    return [
        [get_progress_frame()],
        [get_output_options()],
        [get_column([[prompt_tabs]]),get_column(utilities())]
        ]



