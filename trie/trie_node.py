class TrieNode:
    """
    A Node in a Trie (Suffix Tree)
    edges represents this node's child nodes
    is_suffix_end indicates if this node is the end of a suffix
    """
    
    def __init__(self, length_edges: int) -> None:
        self.edges = [None] * length_edges
        self.is_suffix_end = False