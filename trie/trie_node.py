from multiprocessing.sharedctypes import Value


class TrieNode:
    """
    A Node in a Trie (Suffix Tree)
    edges represents this node's child nodes
    is_suffix_end indicates if this node is the end of a suffix
    Raises ValueError if length_edges is negative
    """
    
    def __init__(self, length_edges: int) -> None:
        if length_edges < 0:
            raise ValueError("length_edges must be positive!")
        self.edges = [None] * length_edges
        self.is_suffix_end = False