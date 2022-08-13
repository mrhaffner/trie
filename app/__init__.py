from flask import Flask
from trie.standard_trie import StandardTrie


trie = StandardTrie(200)

def create_app():
    app = Flask(__name__)

    from app.routes import bp

    app.register_blueprint(bp)

    return app