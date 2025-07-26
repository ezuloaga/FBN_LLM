import lmstudio as lms


# SERVER_API_HOST = "192.168.1.29:1234"
# lms.configure_default_client(SERVER_API_HOST)

def llm_server():
    client = lms.get_default_client()
    print(client.api_host)

# # List downloaded models
def list_downloaded_modules():
    downloaded = lms.list_downloaded_models()
    llm_only = lms.list_downloaded_models("llm")
    embedding_only = lms.list_downloaded_models("embedding")

    print('downloaded models:')
    for model in downloaded:
        print(model)


# List Loaded Models
def list_loaded_modules():
    downloaded = lms.list_loaded_models()
    print('loaded models:')
    all_loaded_models = lms.list_loaded_models()
    llm_only = lms.list_loaded_models("llm")
    embedding_only = lms.list_loaded_models("embedding")
    print(all_loaded_models)

# get current model
def get_current_model():
    print('Current model')
    print(lms.llm)

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

def send_prompt(user_prompt,lm_studio_server,model_to_use):
    lms.configure_default_client(lm_studio_server)
    model = lms.llm(model_to_use)
    result = model.respond(user_prompt)
    print(result)
    return result


# list_downloaded_modules()
# list_loaded_modules()
# get_current_model()
# unload_model()
# check_model()
# load_model()
# llm_server()

