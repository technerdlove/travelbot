# DEVELOPMENT ENVIRONMENT
# Python 3.6 (you can download this here: https://www.python.org/downloads/)
# Pip (you can download this here: https://pypi.python.org/pypi/pip)

# Once you have downloaded the above files, you need to install the following libraries:
# pip3 install Flask==0.12.2
# pip3 install pymessenger==0.0.7.0


# ======= Coding Our Bot =========

# 1. Here I create a basic Flask app. 
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
# 2. we will use GET requests when Facebook checks the bot’s verify token

if request.method == 'GET':
    # Before allowing people to message your bot, Facebook has implemented a verify token
    # that confirms all requests that your bot receives came from Facebook. 
    token_sent = request.args.get("hub.verify_token")
    return verify_fb_token(token_sent)

# what is “hub.verify_token”? 
# This refers to a token we will make up and also provide to Facebook 
# that they will use to verify the bot only responds to requests sent from Messenger. 


# 3. If the bot is not receiving a GET request, 
# it is likely receiving a POST request where Facebook is sending your bot a message sent by a user.

# if the request was not get, it must be POST and we can just proceed with sending a message # back to user
   else:
        # get whatever message a user sent the bot
       output = request.get_json()
       for event in output['entry']:
          messaging = event['messaging']
          for message in messaging:
            if message.get('message'):
                #Facebook Messenger ID for user so we know where to send response back to
                recipient_id = message['sender']['id']
                if message['message'].get('text'):
                    response_sent_text = get_message()
                    send_message(recipient_id, response_sent_text)
                #if user sends us a GIF, photo,video, or any other non-text item
                if message['message'].get('attachments'):
                    response_sent_nontext = get_message()
                    send_message(recipient_id, response_sent_nontext)
    return "Message Processed"


# 4. we move on to handle verifying a message from Facebook as well as generating and sending a response back to the user. 
# Facebook requires that your bot have a verify token that you also provide to them 
# in order to ensure all requests your bot receives originated from them:

def verify_fb_token(token_sent):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error 
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'

# 5. Once we know what we are sending back to the user, 
# we need to write a method that actually sends this message to the user. 
# The PyMessenger library makes this easier for us by handling the POST requests per the Messenger API.

def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"



