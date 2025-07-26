import lmstudio as lms

# remote = "192.168.1.29:1234"
# local = "localhost:1234"
# llm_server_to_prompt = local
# lms.configure_default_client(llm_server_to_prompt)

def llm_server():
    client = lms.get_default_client()
    result = client.api_host
    # print(type(result))
    # print(result)
    return result




# List Loaded Models
def list_loaded_models():
    all_loaded_models = lms.list_loaded_models()
    llm_only = lms.list_loaded_models("llm")
    embedding_only = lms.list_loaded_models("embedding")

    print(all_loaded_models)

# get current model
def get_current_model():
    model = lms.llm()
    print(model)
    return model
    # retrun model
    # print('Current model')


# Unload model
def unload_model():
    try:
        print('Unloading model')
        model = lms.llm()
        model.unload()
        print('model unloaded')
    except:
        print(check_model())


# Check model
def check_model():
    try:
        model = lms.llm()
        print(model)
    except Exception as e:
        print(e)

def load_model():
    model = lms.llm("deepseek/deepseek-r1-0528-qwen3-8b")
    print(get_current_model())
    print(lms.llm)

def text_prompt(user_prompt,llm_server_to_prompt,model_to_use):
    lms.configure_default_client(llm_server_to_prompt)
    model = lms.llm(model_to_use)
    result = model.respond(user_prompt)
    print(result)
    return result

def describe_image_prompt(user_prompt,llm_server_to_prompt,model_to_use,image_file):
    lms.configure_default_client(llm_server_to_prompt)
    model = lms.llm(model_to_use)
    result = model.respond(user_prompt)
    image_handle = lms.prepare_image(image_file)
    chat = lms.Chat()
    chat.add_user_message(user_prompt, images=[image_handle])
    prediction = model.respond(chat)
    # print(prediction)
    return prediction


# # List downloaded models
def list_downloaded_models():
    downloaded = lms.list_downloaded_models()
    llm_only = lms.list_downloaded_models("llm")
    embedding_only = lms.list_downloaded_models("embedding")
    print('downloaded models:')
    for model in downloaded:
        print(model)

# llm_server()

# list_downloaded_models()

# get_current_model()

# list_loaded_models()

