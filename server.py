import sys
import beatbox
from flask import Flask

app = Flask(__name__)

# hard-coded app settings
login = 'jean.marie.comets@gmail.com'
password = 'saucebolo42'
token = 'eorLqTAvZKwy0UwG8IfQ1UNo'

# login to salesforce
svc = beatbox.PythonClient()
svc.login(login, password + token)

@app.route('/')
def index():
    return """
<pre>
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
</pre>
"""

if __name__ == '__main__':
    app.run('0.0.0.0',
            port=8888,
            debug=True,
            #ssl_context='adhoc'
            )
