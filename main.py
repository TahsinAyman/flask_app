from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello Word...</h1>"

app.run(debug=True, host="0.0.0.0", port=8080)
