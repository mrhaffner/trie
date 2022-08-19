import math

from typing import List
from trie.cached_trie_node import CachedTrieNode
from trie.weighted_trie import SuffixEntry, WeightedTrie


class CachedTrie(WeightedTrie):
    """
    A Cached Trie is a variant of a Weighted Trie.
    All nodes in the Trie contain a cache.
    The length of the cache is limited to the size of the limit property.
    The cache contains a list of valid suffixes in its
        subtree. The cache is sorted by weight.  The empty string
        will always appear first if the root of a subtree is itself a 
        valid suffix (except for the root of the Trie itself).
    Raises ValueError if limit < 1
    """

    SIZE_CHAR_SET = 27

    def __init__(self, limit, max_depth: int = math.inf) -> None:
        if max_depth < 0:
            raise ValueError("max_depth must be a positive integer")
        if limit < 1:
            raise ValueError("limit must be >= 1")

        self._limit = limit
        self._root = self._create_node()
        # automatically includes the empty string
        self._root.weight = 1
        self._max_depth = max_depth
        self.cache = []


    def _create_node(self) -> CachedTrieNode:
        return CachedTrieNode(CachedTrie.SIZE_CHAR_SET)


    def insert(self, suffix_dict: SuffixEntry) -> bool:
        """"""
        if super().insert(suffix_dict) == False:
            return False

        cur_node = self._root

        for char in suffix_dict["suffix"]:
            new_cache = self._get_suffixes_from_node(cur_node)
            new_cache.sort(reverse=True, key=lambda d: d["weight"])
            if len(new_cache) > self._limit:
                new_cache = new_cache[:self._limit]
            
            cur_node.cache = new_cache

            hash_code = self._hash_char(char)
            cur_node = cur_node.edges[hash_code]

        return True


    def delete(self, suffix: str) -> bool:
        """"""
        if super().delete(suffix) == False:
            return False

        cur_node = self._root

        for char in suffix:
            new_cache = self._get_suffixes_from_node(cur_node)
            new_cache.sort(reverse=True, key=lambda d: d["weight"])
            if len(new_cache) > self._limit:
                new_cache = new_cache[:self._limit]
            
            cur_node.cache = new_cache

            hash_code = self._hash_char(char)
            cur_node = cur_node.edges[hash_code]

            if cur_node is None:
                break

        return True


    def get_suffixes(self, prefix: str = "") -> List[str]:
        """"""
        node = self._get_node_from_str(prefix)
        
        if node is None:
            return []

        suffix_dicts = node.cache
        return [d["suffix"] for d in suffix_dicts]