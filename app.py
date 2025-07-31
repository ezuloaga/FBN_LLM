from flask import Flask, render_template, redirect, url_for, session, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

from utils.llm_prompt import text_prompt, describe_image_prompt
from utils.llm_utils import RunUtility
from utils.auth_utils import login_required

app = Flask(__name__)
app.secret_key = 'a053a0d115c800cd177474dc7c4a0646'  # Required for CSRF protection and sessions
app.permanent_session_lifetime = timedelta(days=30)

# Configure SQLite and SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# --- Database Models ---
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)


# --- Forms ---
class TextPromptForm(FlaskForm):
    name = StringField('What do you want to ask?', validators=[DataRequired()])
    submit = SubmitField('Submit')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


# --- Routes ---
@app.route('/')
@app.route('/home')
def home():
    page_title = 'Welcome to FatGPT'
    return render_template('home.html', page_title=page_title)

@app.route('/describe_image')
def llm_describe_image():
    page_title = "Image Prompt"

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

    result = describe_image_prompt(user_prompt, lm_studio_host, model_to_use, image_file)

    return render_template(
        'describe_image.html',
        image_file=image_file,
        page_title=page_title,
        result=result,
        model_to_use=model_to_use,
        user_prompt=user_prompt,
        lm_studio_host=lm_studio_host
    )

@app.route('/run_util')
@login_required
def run_util():
    page_title = "App Utilities"
    # lm_studio_host = "localhost:1234"
    lm_studio_host = "192.168.1.29:1234"
    RunUtility.get_server_address(lm_studio_host=lm_studio_host)
    # result_type = type(RunUtility.get_server_address(lm_studio_host=lm_studio_host))
    return render_template(
        'run_util.html',
        page_title=page_title,
        lm_studio_host=lm_studio_host
    )

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
        user_prompt = form.name.data
        result = text_prompt(user_prompt, lm_studio_host, model_to_use)

        return render_template(
            'text_prompt.html',
            page_title=page_title,
            result=result,
            model_to_use=model_to_use,
            user_prompt=user_prompt,
            lm_studio_host=lm_studio_host
        )
    return render_template(
        'text_prompt_form.html',
        form=form,
        page_title=page_title,
        model_to_use=model_to_use,
        lm_studio_host=lm_studio_host
    )

# --- Authentication Routes ---
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists.', 'warning')
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful. Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', form=form, page_title="Register")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password_input = form.password.data

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password_input):
            session['user_id'] = user.id
            session['username'] = user.username

            session.permanent = form.remember.data

            flash('Logged in successfully.', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password.', 'danger')

    return render_template('login.html', form=form, page_title="Login")

@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully.', 'info')
    return redirect(url_for('home'))


# # --- Run ---
if __name__ == '__main__':
    app.run(debug=True)

