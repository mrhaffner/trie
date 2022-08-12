from flask import Flask, jsonify, request
from trie.standard_trie import StandardTrie
import urllib.parse


trie = StandardTrie(200)

app = Flask(__name__)


@app.route("/api", methods=["GET"])
def index():
    return jsonify("Welcome to the API.")


@app.route("/api/trie", methods=["GET"])
def contains_suffix():
    suffix_arg = request.args.get("suffix")
    if not suffix_arg:
        return "", 400
    # if no prefix is given, return all suffixes
    suffix = urllib.parse.unquote(suffix_arg) if suffix_arg else None

    contains_suffix = trie.contains(suffix) if suffix else False

    if contains_suffix:
        return "", 200

    return "", 404


@app.route("/api/trie", methods=["POST"])
def post_suffix():
    # responds with 400 if no suffix
    suffix = request.form["suffix"]
    success = trie.insert(suffix)

    if not success:
        return "", 422

    return jsonify({"suffix": suffix})

# spaces!!!

@app.route("/api/trie", methods=["DELETE"])
def delete_suffix():
    # responds with 400 if no suffix
    suffix = request.form["suffix"]
    success = trie.delete(suffix)
    
    if not success:
        return "", 422

    return "", 204


@app.route("/api/trie/suggestions", methods=["GET"])
def get_suggestions():
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