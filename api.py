import json
from flask import Flask, jsonify, request
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


@app.route("/trie", methods=["GET"])
def query_trie():
    prefix = request.args.get("prefix")
    number = request.args.get("number")
    suggestions = t.get_suggestions(prefix)
    output = suggestions[:int(number)] if number else suggestions

    return jsonify(output)


@app.route("/trie", methods=["POST"])
def add_word():
    word = json.loads(request.data)
    t.add(word)
    return "", 200

app.run()