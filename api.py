import json
import urllib.parse

from flask_cors import CORS
from flask import Flask, jsonify, request
from trie import Trie

t = Trie()

with open("search_terms.json", "r") as f:
    terms = json.loads(f.read())
    for term in terms:
        t.add(term["term"])


app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return "Welcome to the API."


@app.route("/trie", methods=["GET"])
def query_trie():
    prefix = urllib.parse.unquote(request.args.get("prefix"))
    limit = request.args.get("limit")
    suggestions = t.get_suggestions(prefix)
    output = suggestions[:int(limit)] if limit else suggestions
    return jsonify(output)


@app.route("/trie", methods=["POST"])
def add_word():
    word = json.loads(request.data)
    t.add(word)
    return "", 200


if __name__ == "__main__":
    app.run()