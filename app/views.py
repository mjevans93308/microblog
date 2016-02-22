
from app import App

@App.route('/')
@App.route('/index')
def index():
    user = {'nickname': 'Matt'}
    return '''
<html>
    <head>
        <title>Home Page</title>
    </head>
    <body>
        <h1>Hello, ''' + user['nickname'] + '''</h1>
    <body>
</html>
'''
