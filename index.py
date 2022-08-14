from flask import Flask, jsonify
from svm import Process


app = Flask(__name__);
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True


@app.route("/rdy/sastrawi", methods=["POST"])
def post_text():
    return Process();


app.run()