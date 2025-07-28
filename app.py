from flask import Flask, render_template
from utils.llm_prompt import text_prompt, describe_image_prompt
from utils.llm_utils import RunUtility
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'a053a0d115c800cd177474dc7c4a0646'  # Required for CSRF protection


@app.route('/')
@app.route('/home')
def home():
    page_title = 'Welcome to FatGPT'
    return render_template(
        'home.html',
        page_title=page_title)


@app.route('/describe_image')
def llm_describe_image():
    page_title="Image Prompt"

    # lm_studio_host = "192.168.1.29:1234" # Remote
    lm_studio_host = "localhost:1234" # Local
    model_to_use="qwen2-vl-2b-instruct" # Local
    # model_to_use="google/gemma-3-12b" # Local/Remote

    # image_file = "user_uploads/screenshot.png"
    # user_prompt = "is there a car in this screenshot?"

    # image_file = "user_uploads/tina.jpeg"
    # user_prompt = "is there a dog in this image?"

    image_file = "user_uploads/rav4.jpeg"
    user_prompt = "is there a car in this image?"

    result = describe_image_prompt(user_prompt,lm_studio_host,model_to_use,image_file)

    return render_template(
        'describe_image.html',
        image_file=image_file,
        page_title=page_title,
        result=result,
        model_to_use=model_to_use,
        user_prompt=user_prompt,
        lm_studio_host=lm_studio_host)


@app.route('/run_util')
def run_util():
    page_title = "App Utilities"
    # lm_studio_host = "localhost:1234"
    lm_studio_host = "192.168.1.29:1234"
    RunUtility.get_server_address(lm_studio_host=lm_studio_host)
    # result_type = type(RunUtility.get_server_address(lm_studio_host=lm_studio_host))
    return render_template(
        'run_util.html',
        page_title=page_title,
        lm_studio_host=lm_studio_host)


# Define the form
class TextPromptForm(FlaskForm):
    name = StringField('What do you want to ask?', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/text_prompt', methods=['GET', 'POST'])
def llm_text_prompt():
    form = TextPromptForm()
    page_title = 'Ask the LLM for something'
    # model_to_use = "google/gemma-3-12b"  # Local/Remote
    model_to_use = "deepseek/deepseek-r1-0528-qwen3-8b"  # Local/Remote
    lm_studio_host = "localhost:1234"  # Local
    # lm_studio_host = "192.168.1.29:1234"  # Remote
    if form.validate_on_submit():
        page_title = 'Text Prompt Result'
        name = form.name.data
        user_prompt = form.name.data
        result = text_prompt(user_prompt, lm_studio_host, model_to_use)

        return render_template(
            'text_prompt.html',
            page_title=page_title,
            result=result,
            model_to_use=model_to_use,
            user_prompt=user_prompt,
            lm_studio_host=lm_studio_host)
    return render_template(
        'text_prompt_form.html',
        form=form,
        page_title=page_title,
        model_to_use=model_to_use,
        lm_studio_host=lm_studio_host)


if __name__ == '__main__':
    app.run()
