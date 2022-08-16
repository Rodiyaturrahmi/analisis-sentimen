# from flask import Flask, jsonify
import json
from svm import Process
from nbc import analisnbc

app = Flask(__name__);
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True


@app.route("/rdy/sastrawi", methods=["POST"])
def post_text():
    return Process();

@app.route("/rdy/sastrawi", methods=["GET"])
def get_text():
    return analisnbc();



app.run()
