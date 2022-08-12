from flask import Flask, jsonify, request
from trie.standard_trie import StandardTrie
import urllib.parse


trie = StandardTrie(200)

app = Flask(__name__)


@app.route("/api", methods=["GET"])
def index() -> None:
    """Returns a message welcoming you to the API base route"""
    return jsonify("Welcome to the API.")


@app.route("/api/trie", methods=["GET"])
def contains_suffix() -> None:
    """
    Indicates whether the Trie contains the given suffix with a status code
    Format: GET /api/trie?suffix=the-suffix-you-are-looking-for
    Response status codes:
        200: The Trie contains the suffix
        400: A suffix arguement was not given
        404: The Trie does not contain the suffix
    """
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
def post_suffix() -> None:
    """
    Adds a suffix to the Trie
    JSON POST format: {"suffix": "the-suffix-you-want-to-add"}
    Response status codes:
        200: The suffix was added to the Trie
        400: A suffix arguement was not given
        422: The suffix was not added to the Trie (invalid suffix)
    """
    suffix = request.form["suffix"]
    success = trie.insert(suffix)

    if success:
        return jsonify({"suffix": suffix})
    return "", 422



@app.route("/api/trie", methods=["DELETE"])
def delete_suffix() -> None:
    """
    Deletes a suffix from the Trie
    JSON DELETE format: {"suffix": "the-suffix-you-want-to-delete"}
    Response status codes:
        204: The suffix was deleted from the Trie
        400: A suffix arguement was not given
        422: The suffix was not deleted from the Trie (suffix invalid or not in trie)
    """
    suffix = request.form["suffix"]
    success = trie.delete(suffix)
    
    if not success:
        return "", 422

    return "", 204


@app.route("/api/trie/suggestions", methods=["GET"])
def get_suggestions() -> None:
    """
    Returns all possible suffixes for a given prefix in a JSON list
    Format: GET /api/trie/suggestions?prefix=the-prefix-you-are-looking-for
            GET /api/trie/suggestions (prefix = "", returns all suffixes in the Trie)
    Response status codes:
        200: Indicates a successful retrieval (including no suggestions)
    """
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