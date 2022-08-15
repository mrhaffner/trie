import json

from flask import Flask
from flask_cors import CORS
from pathlib import Path
from trie.standard_trie import StandardTrie


trie = StandardTrie(200) # our database


def functional_testing_setup():
    """Adds a limited set of suffixes to the trie for functional testing"""
    starting_suffixes = ["app", "apple", "apple orchard", "dog"] 
    starting_suffixes += ["z" * i for i in range(2, 16)]
    for suffix in starting_suffixes:
        trie.insert(suffix)


def live_setup():
    """Adds all suffixes from search_terms.json to the Trie"""
    path = Path(__file__).parent.parent.joinpath("search_terms.json")
    with open(path, "r") as f:
        terms = json.loads(f.read())
        for term in terms:
            trie.insert(term["term"])


def create_app(live_server = True):
    """
    Returns your Flask App with setup for Live or Testing.
    For unittests, live_server should be False - leaves Trie empty.
    For functional tests, set live_server to True and DEBUG to False.
        Adds suffixes to the trie for functional tests.
    Default settings of live_server = True and debug = False adds the
        full set of search_terms to the Trie.
    """
    app = Flask(__name__)
    CORS(app)

    from app.routes import bp

    app.register_blueprint(bp)

    if app.config["DEBUG"] == False and live_server == True:
        live_setup()
    if app.config["DEBUG"] == True and live_server == True:
        functional_testing_setup()

    return app

app = create_app()
