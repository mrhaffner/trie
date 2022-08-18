class WeightedTrieNode:
    """
    A Node in a Weighted Trie (Suffix Tree)
    edges represents this node's child nodes
    weight >= 1 indicates this node is the end of a suffix
    weight represents the relative occurance of a given suffix
    Raises ValueError if length_edges is negative
    """

    def __init__(self, length_edges) -> None:
        if length_edges < 0:
            raise ValueError("length_edges cannot be negative")
        self.edges = [None] * length_edges
        self.weight = 0