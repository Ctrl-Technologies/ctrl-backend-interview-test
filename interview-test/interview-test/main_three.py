# Flask framework
from flask import Flask, url_for
import json
import platform
import locale
locale.setlocale(locale.LC_ALL, str('en_US.UTF-8'))

app = Flask(__name__)


def list_routes():
    import urllib.parse
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.parse.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, url))
        output.append(line)
    return sorted(output)

# Substituting a database system here for test
user = [(1, {'username': 'SolidSnake', 'email': 'a@a.com', 'balance': 1600.0}),
        (2, {'username': 'HanSolo', 'email': 'b@b.com', 'balance': 1500.0}),
        (3, {'username': 'Rick', 'email': 'c@c.com', 'balance': 0.0})
        ]

#example of auth token for SolidSnake
auth_tokens = [(1, 'xxxxxx')]

"""
Lets assume you are building the auth yourself or using a framework's auth. You can get creative and use whatever 
you need.

I am not testing a in depth-knowledge of flask ,merely thinking behind building na API.

To test the API I recommend using Insomnia or Postman:https://www.getpostman.com/apps or https://insomnia.rest/download/

If I have create a example endpoint on the root endpoint http://localhost:8000/ and health endpoint 
http://localhost:8000/health

Add a authentication endpoint 
 * POST request with email and password
 * Returns a auth token to user and stores it

Add a GET user endpoint (retrieve user)
 * Requires authenticated user (Header with Authorization:token

Add a POST user endpoint to create a new user
* This requires a POST request capturing the email, username and password
* returns auth token much like authentication

Add a GET with auth to get the user's balance

Bonus: one POST request for both credit and debit. Hint query/params 

"""

@app.route('/', methods=['GET'])
def root():
    return app.response_class(
        json.dumps({
            "message": "Welcome to the Ctrl API test",
            "endpoints": list_routes()
        })
    )

@app.route('/health', methods=['GET'])
def health():
    platform_string = "{} - {} - {}".format(
        # platform.machine(),
        # platform.version(),
        # platform.platform(),
        platform.uname(),
        platform.system(),
        platform.processor()
    )
    return app.response_class(
        json.dumps({
            "message": "I seem to be healthy",
            "whoami": platform_string
        })
    )





