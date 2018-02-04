# ======= Coding Our Bot =========

# Here I create a basic Flask app. 
# Flask is a web framework for Python, read more here: http://flask.pocoo.org/docs/0.12/quickstart/

from flask import Flask, request

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def receive_message():
    return "Hello World!"


if __name__ == '__main__':
    app.run()
    
    
# Now, run from the command line by typing python3 app.py
# You should see something like this:  
# * Running on http://127.0.0.1:5000/ (Press CTRL C to quit)

# If you navigate to the link given from running the app (in this example http://127.0.0.1:5000/) in a browser, 
# you will see a page load that says “Hello World!” 

# ======= From Basic Flask app to Bot =========

