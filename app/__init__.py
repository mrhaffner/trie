from flask import Flask
from trie.standard_trie import StandardTrie


trie = StandardTrie(200)

# for testing
starting_suffixes = ["app", "apple", "apple orchard", "dog"] 
starting_suffixes += ["z" * i for i in range(2, 16)]
for suffix in starting_suffixes:
    trie.insert(suffix)

def create_app():
    app = Flask(__name__)

    from app.routes import bp

    app.register_blueprint(bp)

    return app

