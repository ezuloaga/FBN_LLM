from flask import Flask, render_template, url_for, send_from_directory
import os
# import lmstudio as lms
from utils.llm_utils import text_prompt, describe_image_prompt, llm_server, list_loaded_models

app = Flask(__name__)
UPLOAD_FOLDER = 'user_uploads/'

remote = "192.168.1.29:1234"
local = "localhost:1234"

@app.route('/upload_folder')
def upload_folder():  # put application's code here
    return UPLOAD_FOLDER


@app.route('/')
@app.route('/home')
def home():
    page_title = 'Welcome to FatAI'
    return render_template('home.html',page_title=page_title)

@app.route('/text_prompt')
def llm_text_prompt():
    page_title = 'Fat GPT | Text Prompt'
    llm_server_to_prompt = remote
    user_prompt = "give me a bulleted list of numbers from 1 to 20 and be quick and brief"
    # user_prompt = "what are the benefits to using flask blueprints?"
    model_to_use="deepseek/deepseek-r1-0528-qwen3-8b"
    # model_to_use="google/gemma-3-12b"
    result = text_prompt(user_prompt,llm_server_to_prompt,model_to_use)
    return render_template('text_prompt.html', page_title=page_title, result=result, model_to_use=model_to_use, user_prompt=user_prompt, llm_server_to_prompt=llm_server_to_prompt)


@app.route('/describe_image')
def llm_describe_image():
    # return 'decribe image'
    page_title="FatGPT | Describe an image"
    image_file = "user_uploads/screenshot.png"
    file_name = 'screenshot.png'
    llm_server_to_prompt = local
    user_prompt = "please describe what is in this image"
    model_to_use="qwen2-vl-2b-instruct"
    result = describe_image_prompt(user_prompt,llm_server_to_prompt,model_to_use,image_file)
    image_for_show = send_from_directory(UPLOAD_FOLDER, file_name)
    return render_template('describe_image.html',image_file=image_file, page_title=page_title, result=result,model_to_use=model_to_use,user_prompt=user_prompt,llm_server_to_prompt=llm_server_to_prompt, image_for_show=image_for_show)
    # return image_for_show

@app.route('/run_util')
def run_util():
    page_title = "FatGPT | Utility Test"
    # result = llm_server() # utility function
    result = list_loaded_models() # utility function
    result_type = type(result)
    return render_template('run_util.html', page_title=page_title, result=result, result_type=result_type)




if __name__ == '__main__':
    app.run()


# list_downloaded_models()
# list_loaded_models()
# get_current_model()
# unload_model()
# check_model()
# load_model()
# llm_server()
