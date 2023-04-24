from flask import Flask, render_template, request, url_for, Markup, jsonify

#Initialize the flask App
app = Flask(__name__)

from routes import *

if __name__ == "__main__":
    app.run(debug=True)