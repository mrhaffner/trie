from flask import Flask, jsonify, request
from trie.standard_trie import StandardTrie
import urllib.parse


starting_suffixes = ["app", "apple", "apple orchard", "dog"]

trie = StandardTrie(200)
for suffix in starting_suffixes:
    trie.insert(suffix)

app = Flask(__name__)


@app.route("/api", methods=["GET"])
def index():
    return jsonify("Welcome to the API.")


@app.route("/api/trie", methods=["GET"])
def get_suffixes():
    prefix_arg = request.args.get("prefix")
    # if no prefix is given, return all suffixes
    prefix = urllib.parse.unquote(prefix_arg) if prefix_arg else ""

    suffixes = trie.get_suffixes(prefix)
    limit_arg = request.args.get("limit")
    limit = None

    if limit_arg and int(limit_arg) < len(suffixes):
        limit = int(limit_arg)

    response = suffixes[0:limit] if limit else suffixes
    return jsonify(response)