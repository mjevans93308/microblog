
from app import App

@App.route('/')
@App.route('/index')
def index():
    return "Hello, World!"