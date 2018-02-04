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

# To handle sending messages back to a user who communicates with our bot, 
# use the PyMessenger library to handle sending responses to users.
# First need to handle two types of requests, GET and POST
# we will use GET requests when Facebook checks the bot’s verify token

if request.method == 'GET':
    # Before allowing people to message your bot, Facebook has implemented a verify token
    # that confirms all requests that your bot receives came from Facebook. 
    token_sent = request.args.get("hub.verify_token")
    return verify_fb_token(token_sent)

# what is “hub.verify_token”? 
# This refers to a token we will make up and also provide to Facebook 
# that they will use to verify the bot only responds to requests sent from Messenger. 


