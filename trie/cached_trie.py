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
        suffix = suffix_dict["suffix"]
        weight = suffix_dict["weight"]

        if not self._is_valid_suffix(suffix):
            return False
        
        cur_node = self._root

        for char in suffix:
            self._update_cache(cur_node, suffix, weight)
            suffix = suffix[1:]
            hash_code = self._hash_char(char)

            # create new node if char not in trie
            if not cur_node.edges[hash_code]:
                cur_node.edges[hash_code] = self._create_node()

            cur_node = cur_node.edges[hash_code]

        # mark the end of the suffix
        cur_node.weight = weight
        self._update_cache(cur_node, suffix, weight)

        return True


    def _update_cache(self, node: CachedTrieNode, suffix: str, weight: int) -> None:
        """"""
        suffix_dict: SuffixEntry = {"suffix": suffix, "weight": weight}
        node.cache.append(suffix_dict)
        node.cache.sort(reverse=True, key=lambda d: d["weight"])
        if len(node.cache) > self._limit:
            node.cache = node.cache[:self._limit]


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