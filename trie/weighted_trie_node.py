class WeightedTrieNode():

    def __init__(self, length_edges):
        if length_edges < 0:
            raise ValueError("length_edges cannot be negative")
        self.edges = [None] * length_edges
        self.weight = 0