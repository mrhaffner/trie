from flask import Flask, jsonify
from trie import Trie

t = Trie()

t.add("Apple")
t.add("AppleOrchard")
t.add("Doggo")
t.add("Apple Orchard")

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the API."


@app.route('/trie/<string:word>')
def trie(word):
    return jsonify(t.get_suggestions(word))


app.run()