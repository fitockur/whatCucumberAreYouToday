from flask import Flask, request, jsonify
from cucumber_scrapper import cucumber_scrapper
import yaml


app = Flask(__name__)

@app.route('/getmsg/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    name = request.args.get("name", None)

    # For debugging
    print(f"got name {name}")

    response = {}

    # Check if user sent a name at all
    if not name:
        response["ERROR"] = "no name found, please send a name."
    # Check if the user entered a number not a name
    elif str(name).isdigit():
        response["ERROR"] = "name can't be numeric."
    # Now the user entered a valid name
    else:
        response["MESSAGE"] = f"Welcome {name} to our awesome platform!!"

    # Return the response in json format
    return jsonify(response) 

@app.route('/cucumbers/')
def get_cucumbers():
    with open('cucumbers.yml', 'r', encoding='utf-8') as f:
        cucumbers = yaml.safe_load(f)

    # Return the response in json format
    return jsonify(cucumbers)

# A welcome message to test our server
@app.route('/')
def index():
    return "Welcome to our server !!"

if __name__ == '__main__':
    with open('cucumbers.yml', 'w', encoding='utf-8') as f:
        yaml.safe_dump(cucumber_scrapper(), f)
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
