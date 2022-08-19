import math

from trie.standard_trie import StandardTrie
from trie.weighted_trie_node import WeightedTrieNode
from typing import List, TypedDict


class SuffixEntry(TypedDict):
    suffix: str
    weight: int


class WeightedTrie(StandardTrie):
    """
    A Weighted Trie is a variant of a Trie with weighted nodes.
    The Weighted Trie differs in that:
        1. A valid string in the trie is found by following a path from root to
            a child node with weight > 0
        2. Gettings suffixes returns output sorted descending by weight.
           If a given prefix is itself a valid suffix, the empty string will
           appear as a valid suffix (but not for _root).
        3. Due to the sorting of suffixes, getting suffixes from a Weighted Trie is 
           slower than from a Standard Trie
    """

    def __init__(self, max_depth: int = math.inf) -> None:
        if max_depth < 0:
            raise ValueError("max_depth must be a positive integer")

        self._root = self._create_node()
        # automatically includes the empty string
        self._root.weight = 1
        self._max_depth = max_depth


    def _create_node(self) -> WeightedTrieNode:
        return WeightedTrieNode(StandardTrie.SIZE_CHAR_SET)


    def insert(self, suffix_dict: SuffixEntry) -> bool:
        """
        Inserting a suffix that already exists in this trie will update its weight.
        Adding a suffix with weight less than 1 will may add nodes to this trie, but it
            will not exist as a valid suffix in this trie. If that suffix already exits
            in this trie, it will effectively delete it.
        """
        suffix = suffix_dict["suffix"]
        weight = suffix_dict["weight"]

        if not self._is_valid_suffix(suffix):
            return False
        
        cur_node = self._root

        for char in suffix:
            hash_code = self._hash_char(char)

            # create new node if char not in trie
            if not cur_node.edges[hash_code]:
                cur_node.edges[hash_code] = self._create_node()

            cur_node = cur_node.edges[hash_code]

        # mark the end of the suffix
        cur_node.weight = weight

        return True


    def contains(self, suffix: str) -> bool:
        node = self._get_node_from_str(suffix)

        if node is None or node.weight == 0:
            return False
        else:
            return True


    def delete(self, suffix: str) -> bool:
        # cannot delete empty string
        if suffix == "":
            return False

        node = self._get_node_from_str(suffix)
        
        if node is None:
            return False

        node.weight = 0
        return True


    def get_suffixes(self, prefix: str = "") -> List[str]:
        """Output is sorted ascending by weight"""
        node = self._get_node_from_str(prefix)
        
        if node is None:
            return []

        suffix_dicts = self._get_suffixes_from_node(node)
        suffix_dicts.sort(reverse=True, key=lambda d: d["weight"])
        return [d["suffix"] for d in suffix_dicts]


    def _get_suffixes_from_node(self, node: WeightedTrieNode, suffix = "", suffixes = None) -> List[SuffixEntry]:
        """
        Returns an array of all suffix entries from a given root node.
        """
        if suffixes is None:
            suffixes = []

        # do not add "" to suffixes if _root
        if node.weight > 0 and node != self._root:
            suffixes.append({"suffix": suffix, "weight": node.weight})

        for idx, node in enumerate(node.edges):
            if node:
                self._get_suffixes_from_node(node, suffix + self._reverse_hash_char(idx), suffixes)

        return suffixes