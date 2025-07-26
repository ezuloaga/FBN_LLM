from flask import Flask, render_template
# import lmstudio as lms
from utils.llm_utils import send_prompt, image_prompt

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/text_prompt')
def llm():  # put application's code here
    page_title = 'FatGPT | Text Prompt'
    remote = "192.168.1.29:1234"
    local = "localhost:1234"
    llm_server_to_prompt = local
    # user_prompt = "give me a bulleted list of numbers from 1 to 20 and be quick and brief"
    user_prompt = "what are the benefits to using flask blueprints?"
    # model_to_use="deepseek/deepseek-r1-0528-qwen3-8b"
    model_to_use="google/gemma-3-12b"
    result = send_prompt(user_prompt,llm_server_to_prompt,model_to_use)
    return render_template('text_prompt.html', page_title=page_title, result=result, model_to_use=model_to_use, user_prompt=user_prompt, llm_server_to_prompt=llm_server_to_prompt)


@app.route('/describe_image')
def llm_image():  # put application's code here
    page_title="FatGPT | Describe an image"
    image_file = "user_uploads/screenshot.png"
    remote = "192.168.1.29:1234"
    local = "localhost:1234"
    llm_server_to_prompt = local
    user_prompt = "please describe what is in this image"
    # model_to_use="deepseek/deepseek-r1-0528-qwen3-8b"
    model_to_use="qwen2-vl-2b-instruct"
    result = image_prompt(user_prompt,llm_server_to_prompt,model_to_use,image_file)
    return render_template('describe_image.html', page_title=page_title, result=result,model_to_use=model_to_use,user_prompt=user_prompt,llm_server_to_prompt=llm_server_to_prompt)


if __name__ == '__main__':
    app.run()


# list_downloaded_modules()
# list_downloaded_modules()
# list_loaded_modules()
# get_current_model()
# unload_model()
# check_model()
# load_model()
# llm_server()
