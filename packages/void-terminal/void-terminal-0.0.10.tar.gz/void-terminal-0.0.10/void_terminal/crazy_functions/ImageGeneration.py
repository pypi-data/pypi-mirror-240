from void_terminal.toolbox import CatchException, update_ui, get_conf, select_api_key, get_log_folder
from void_terminal.crazy_functions.multi_stage.multi_stage_utils import GptAcademicState


def gen_image(llm_kwargs, prompt, resolution="1024x1024", model="dall-e-2"):
    import requests, json, time, os
    from void_terminal.request_llms.bridge_all import model_info

    proxies = get_conf('proxies')
    # Set up OpenAI API key and model 
    api_key = select_api_key(llm_kwargs['api_key'], llm_kwargs['llm_model'])
    chat_endpoint = model_info[llm_kwargs['llm_model']]['endpoint']
    # 'https://api.openai.com/v1/chat/completions'
    img_endpoint = chat_endpoint.replace('chat/completions','images/generations')
    # # Generate the image
    url = img_endpoint
    headers = {
        'Authorization': f"Bearer {api_key}",
        'Content-Type': 'application/json'
    }
    data = {
        'prompt': prompt,
        'n': 1,
        'size': resolution,
        'model': model,
        'response_format': 'url'
    }
    response = requests.post(url, headers=headers, json=data, proxies=proxies)
    print(response.content)
    try:
        image_url = json.loads(response.content.decode('utf8'))['data'][0]['url']
    except:
        raise RuntimeError(response.content.decode())
    # Save the file locally
    r = requests.get(image_url, proxies=proxies)
    file_path = f'{get_log_folder()}/image_gen/'
    os.makedirs(file_path, exist_ok=True)
    file_name = 'Image' + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) + '.png'
    with open(file_path+file_name, 'wb+') as f: f.write(r.content)


    return image_url, file_path+file_name


def edit_image(llm_kwargs, prompt, image_path, resolution="1024x1024", model="dall-e-2"):
    import requests, json, time, os
    from void_terminal.request_llms.bridge_all import model_info

    proxies = get_conf('proxies')
    api_key = select_api_key(llm_kwargs['api_key'], llm_kwargs['llm_model'])
    chat_endpoint = model_info[llm_kwargs['llm_model']]['endpoint']
    # 'https://api.openai.com/v1/chat/completions'
    img_endpoint = chat_endpoint.replace('chat/completions','images/edits')
    # # Generate the image
    url = img_endpoint
    headers = {
        'Authorization': f"Bearer {api_key}",
        'Content-Type': 'application/json'
    }
    data = {
        'image': open(image_path, 'rb'),
        'prompt': prompt,
        'n': 1,
        'size': resolution,
        'model': model,
        'response_format': 'url'
    }
    response = requests.post(url, headers=headers, json=data, proxies=proxies)
    print(response.content)
    try:
        image_url = json.loads(response.content.decode('utf8'))['data'][0]['url']
    except:
        raise RuntimeError(response.content.decode())
    # Save the file locally
    r = requests.get(image_url, proxies=proxies)
    file_path = f'{get_log_folder()}/image_gen/'
    os.makedirs(file_path, exist_ok=True)
    file_name = 'Image' + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) + '.png'
    with open(file_path+file_name, 'wb+') as f: f.write(r.content)


    return image_url, file_path+file_name


@CatchException
def ImageGeneration_DALLE2(prompt, llm_kwargs, plugin_kwargs, chatbot, history, system_prompt, web_port):
    """
    txt             Text entered by the user in the input field，For example, a paragraph that needs to be translated，For example, a file path that contains files to be processed
    llm_kwargs      GPT model parameters，Such as temperature and top_p，Generally pass it on as is
    plugin_kwargs   Plugin model parameters，No use for the time being
    chatbot         Chat display box handle，Displayed to the user
    history         Chat history，Context summary
    system_prompt   Silent reminder to GPT
    web_port        Current software running port number
    """
    history = []    # Clear history，To avoid input overflow
    chatbot.append(("What is this function？", "[Local Message] Generate image, Please switch the model to gpt-* or api2d-* first。If the Chinese effect is not ideal, Try English Prompt。Processing ....."))
    yield from update_ui(chatbot=chatbot, history=history) # Refresh the page # As requesting GPT takes some time，Let`s do a UI update in time
    if ("advanced_arg" in plugin_kwargs) and (plugin_kwargs["advanced_arg"] == ""): plugin_kwargs.pop("advanced_arg")
    resolution = plugin_kwargs.get("advanced_arg", '1024x1024')
    image_url, image_path = gen_image(llm_kwargs, prompt, resolution)
    chatbot.append([prompt,  
        f'Image transfer URL: <br/>`{image_url}`<br/>'+
        f'Transfer URL preview: <br/><div align="center"><img src="{image_url}"></div>'
        f'Local file address: <br/>`{image_path}`<br/>'+
        f'Local file preview: <br/><div align="center"><img src="file={image_path}"></div>'
    ])
    yield from update_ui(chatbot=chatbot, history=history) # Refresh the page # UI update


@CatchException
def ImageGeneration_DALLE3(prompt, llm_kwargs, plugin_kwargs, chatbot, history, system_prompt, web_port):
    history = []    # Clear history，To avoid input overflow
    chatbot.append(("What is this function？", "[Local Message] Generate image, Please switch the model to gpt-* or api2d-* first。If the Chinese effect is not ideal, Try English Prompt。Processing ....."))
    yield from update_ui(chatbot=chatbot, history=history) # Refresh the page # As requesting GPT takes some time，Let`s do a UI update in time
    if ("advanced_arg" in plugin_kwargs) and (plugin_kwargs["advanced_arg"] == ""): plugin_kwargs.pop("advanced_arg")
    resolution = plugin_kwargs.get("advanced_arg", '1024x1024')
    image_url, image_path = gen_image(llm_kwargs, prompt, resolution)
    chatbot.append([prompt,  
        f'Image transfer URL: <br/>`{image_url}`<br/>'+
        f'Transfer URL preview: <br/><div align="center"><img src="{image_url}"></div>'
        f'Local file address: <br/>`{image_path}`<br/>'+
        f'Local file preview: <br/><div align="center"><img src="file={image_path}"></div>'
    ])
    yield from update_ui(chatbot=chatbot, history=history) # Refresh the page # UI update


class ImageEditState(GptAcademicState):
    def get_image_file(self, x):
        import os, glob
        if len(x) == 0:             return False, None
        if not os.path.exists(x):   return False, None
        if x.endswith('.png'):      return True, x
        file_manifest = [f for f in glob.glob(f'{x}/**/*.png', recursive=True)]
        confirm = (len(file_manifest) >= 1 and file_manifest[0].endswith('.png') and os.path.exists(file_manifest[0]))
        file = None if not confirm else file_manifest[0]
        return confirm, file
    
    def get_resolution(self, x):
        return (x in ['256x256', '512x512', '1024x1024']), x
    
    def get_prompt(self, x):
        confirm = (len(x)>=5) and (not self.get_resolution(x)[0]) and (not self.get_image_file(x)[0])
        return confirm, x
    
    def reset(self):
        self.req = [
            {'value':None, 'description': 'Please upload the image first（Must be in .png format）, Then click this plugin again',    'verify_fn': self.get_image_file},
            {'value':None, 'description': 'Please enter the resolution，Optional：256x256, 512x512 or 1024x1024',   'verify_fn': self.get_resolution},
            {'value':None, 'description': 'Please enter modification requirements，It is recommended to use English prompts',                 'verify_fn': self.get_prompt},
        ]
        self.info = ""

    def feed(self, prompt, chatbot):
        for r in self.req:
            if r['value'] is None:
                confirm, res = r['verify_fn'](prompt)
                if confirm:
                    r['value'] = res
                    self.set_state(chatbot, 'dummy_key', 'dummy_value')
                    break
        return self

    def next_req(self):
        for r in self.req:
            if r['value'] is None:
                return r['description']
        return "All information has been collected"

    def already_obtained_all_materials(self):
        return all([x['value'] is not None for x in self.req])

@CatchException
def ImageModification_DALLE2(prompt, llm_kwargs, plugin_kwargs, chatbot, history, system_prompt, web_port):
    history = []    # Clear history
    state = ImageEditState.get_state(chatbot, ImageEditState)
    state = state.feed(prompt, chatbot)
    if not state.already_obtained_all_materials():
        chatbot.append(["Image modification（Upload the image first，Enter modification requirements again，Enter the resolution at last）", state.next_req()])
        yield from update_ui(chatbot=chatbot, history=history)
        return

    image_path = state.req[0]
    resolution = state.req[1]
    prompt = state.req[2]
    chatbot.append(["Image modification, Executing", f"Image:`{image_path}`<br/>Resolution:`{resolution}`<br/>Modify requirements:`{prompt}`"])
    yield from update_ui(chatbot=chatbot, history=history)

    image_url, image_path = edit_image(llm_kwargs, prompt, image_path, resolution)
    chatbot.append([state.prompt,  
        f'Image transfer URL: <br/>`{image_url}`<br/>'+
        f'Transfer URL preview: <br/><div align="center"><img src="{image_url}"></div>'
        f'Local file address: <br/>`{image_path}`<br/>'+
        f'Local file preview: <br/><div align="center"><img src="file={image_path}"></div>'
    ])
    yield from update_ui(chatbot=chatbot, history=history) # Refresh the page # UI update

