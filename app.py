from flask import Flask, render_template, url_for, send_from_directory
import os
# import lmstudio as lms
from utils.llm_utils import text_prompt, describe_image_prompt, llm_server, list_loaded_models

app = Flask(__name__)

remote = "192.168.1.29:1234"
local = "localhost:1234"


@app.route('/')
@app.route('/home')
def home():
    page_title = 'Welcome to FatAI'
    return render_template('home.html',page_title=page_title)


@app.route('/text_prompt')
def llm_text_prompt():
    page_title = 'FatGPT | Text Prompt'
    llm_server_to_prompt = local
    user_prompt = "give me a bulleted list of numbers from 1 to 20 and be fast"
    # user_prompt = "what are the benefits to using flask blueprints?"
    # model_to_use="deepseek/deepseek-r1-0528-qwen3-8b" # remote only
    model_to_use="google/gemma-3-12b" # local and remote
    result = text_prompt(user_prompt,llm_server_to_prompt,model_to_use)
    return render_template('text_prompt.html', page_title=page_title, result=result, model_to_use=model_to_use, user_prompt=user_prompt, llm_server_to_prompt=llm_server_to_prompt)


@app.route('/describe_image')
def llm_describe_image():
    # return 'decribe image'
    page_title="FatGPT | Describe an image"
    image_file = "user_uploads/screenshot.png"
    llm_server_to_prompt = local
    user_prompt = "is there a car in this image?"
    # model_to_use="qwen2-vl-2b-instruct # local only
    model_to_use="google/gemma-3-12b" # local and remote
    result = describe_image_prompt(user_prompt,llm_server_to_prompt,model_to_use,image_file)
    return render_template('describe_image.html',image_file=image_file, page_title=page_title, result=result,model_to_use=model_to_use,user_prompt=user_prompt,llm_server_to_prompt=llm_server_to_prompt)


@app.route('/run_util')
def run_util():
    page_title = "FatGPT | Utility Test"
    # result = llm_server() # utility function
    result = list_loaded_models() # utility function
    result_type = type(result)
    return render_template('run_util.html', page_title=page_title, result=result, result_type=result_type)


@app.route('/upload_image')
def upload_image():
    page_title = "FatGPT | Upload an image"
    return render_template('image_upload.html', page_title=page_title)



if __name__ == '__main__':
    app.run()
