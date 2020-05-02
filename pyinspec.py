import flask
import os

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/',methods=['GET'])
def home():
    return os.system('inspec version')

app.run()