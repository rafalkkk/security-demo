# Errors detected by bandit - docs:
# https://bandit.readthedocs.io/en/latest/plugins/index.html#complete-test-plugin-listing

from flask import Flask, url_for, request, redirect

app = Flask(__name__)

@app.route('/')
def start():
# docume    """Function generates hello_world page"""
    content = f'''<html>
      <body>    
      <h1>6-KINGS-CLUB</h1> 
      <form action = { url_for("login") } method = "post">
      <p>Enter Name:</p>
      <p><input type = "text" name = "nm" /></p>
      <p><input type = "submit" value = "submit" /></p>
      </form>     
      </body>
      </html>
'''
    return f'Hello (6) World<br><br>{content}'


@app.route('/login', methods=['POST', 'GET'])
def login():
# BAD PRACTICE - SILENCED ERROR - B110
    try:
        if request.method == 'POST':
            user = request.form['nm']
            # PASSWORD HARDCODED - B105
            password = "CoffeeWithLemon!"
            return redirect(url_for('success', name=user, pass=password))
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))
    except:
        pass


@app.route('/success/<name>')
def success(name):
    """Function generates the success message"""
    return f'welcome {name} <br><a href={ url_for("start") }>take me home</a>'


@app.route('/failure/<name>')
def failure(name):
    """Function generates the failure message"""
    return f'''Sorry, we don\'t belive you are {name} <br>
<a href={ url_for("start") }>try again</a>'''


if __name__ == '__main__':
    # ERROR - FLASK APPLICATION WORKING IN DEBUG MODE - B201
    app.run(debug=True)
