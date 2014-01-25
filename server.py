import beatbox
from flask import Flask
#from settings import *

app = Flask(__name__)

#login to salesforce
#svc = beatbox.PythonClient()
#svc.login(login, password + token)

# fix for index page
@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/meeting')
def meeting():
    return app.send_static_file('meeting.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=8888,
            debug=True or '--debug' in sys.argv)
