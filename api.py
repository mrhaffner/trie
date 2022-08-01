from flask import Flask, jsonify, request
# from requests import request
from trie import Trie

t = Trie()

t.add("Apple")
t.add("AppleOrchard")
t.add("Doggo")
t.add("Apple Orchard")

app = Flask(__name__)


@app.route("/")
def index():
    return "Welcome to the API."


@app.route("/trie")
def trie():
    prefix = request.args.get("prefix")
    number = int(request.args.get("number"))
    suggestions = t.get_suggestions(prefix)
    output = suggestions[:number] if number else suggestions

    return jsonify(output)


app.run()