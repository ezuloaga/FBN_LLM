from flask import Flask, render_template
# import lmstudio as lms
from utils.llm_utils import send_prompt

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/llm')
def llm():  # put application's code here
    remote_lm_studio = "192.168.1.29:1234"
    local_lm_studio = "localhost:1234"
    user_prompt = "give me a bulleted list of numbers from 1 to 10 and be quick and brief"
    model_to_use="deepseek/deepseek-r1-0528-qwen3-8b"
    # model_to_use="google/gemma-3-12b"
    result = send_prompt(user_prompt,remote_lm_studio,model_to_use)
    return render_template('llm.html', result=result,model_to_use=model_to_use,user_prompt=user_prompt)

if __name__ == '__main__':
    app.run()
