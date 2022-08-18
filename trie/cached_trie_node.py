from typing import List
from trie.weighted_trie import SuffixEntry
from trie.weighted_trie_node import WeightedTrieNode


class CachedTrieNode(WeightedTrieNode):
    """
    Expands upon the WeightedTrieNode with a cache.
    The cache represents valid SuffixEntrys from  this node
        and its children sorted by weight.
    The length of the cache will likely be limited at the Trie 
        level.
    """

    def __init__(self, length_edges) -> None:
        super().__init__(length_edges)
        self.cache: List[SuffixEntry] = []