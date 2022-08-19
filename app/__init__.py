import json

from flask import Flask
from flask_cors import CORS
from pathlib import Path
from trie.cached_trie import CachedTrie
from trie.standard_trie import StandardTrie
from trie.weighted_trie import WeightedTrie

# Our databases
trie = StandardTrie(200)
weighted_trie = WeightedTrie(200)
cached_trie = CachedTrie(10, 200)


def functional_testing_setup():
    """Adds a limited set of suffixes to the tries for functional testing"""
    starting_suffixes = ["app", "apple", "apple orchard", "dog"] 
    starting_suffixes += ["z" * i for i in range(2, 16)]
    for suffix in starting_suffixes:
        trie.insert(suffix)

    suffixes_weighted = [{"suffix": "app", "weight": 1}, {"suffix": "apple", "weight": 4}, 
                         {"suffix": "apple orchard", "weight": 1}, {"suffix": "dog", "weight": 5}] 
    suffixes_weighted += [{"suffix": ("z" * i), "weight": 1} for i in range(2, 16)]
    for suffix in suffixes_weighted:
        weighted_trie.insert(suffix)
        cached_trie.insert(suffix)


def live_setup():
    """Adds all suffixes from search_terms.json to the tries"""
    path = Path(__file__).parent.parent.joinpath("search_terms.json")
    with open(path, "r") as f:
        terms = json.loads(f.read())
        for term in terms:
            suffix = term["term"]
            trie.insert(suffix)
            weighted_entry = {"suffix": suffix, "weight": int(term["hits"])}
            weighted_trie.insert(weighted_entry)
            cached_trie.insert(weighted_entry)


def create_app(live_server = True):
    """
    Returns your Flask App with setup for Live or Testing.
    For unittests, live_server should be False - leaves ries empty.
    For functional tests, set live_server to True and DEBUG to False.
        Adds suffixes to the tries for functional tests.
    Default settings of live_server = True and debug = False adds the
        full set of search_terms to the ries.
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
