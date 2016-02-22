from flask import render_template, flash, redirect
from app import App
from .forms import LoginForm


@App.route('/')
@App.route('/index')
def index():
    user = {'nickname': 'Matt'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'Avengers was cool!'
        },
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@App.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' 
            % (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form, 
                            providers=App.config['OPENID_PROVIDERS'])