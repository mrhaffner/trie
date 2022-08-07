import unittest
from trie import Trie



class TestAddToTrie(unittest.TestCase):

    def setUp(self) -> None:
        self.trie = Trie()

    
    def test_adds_word(self) -> None:
        self.assertTrue(self.trie.add("Apple"))


    # perhaps it should actually return true?
    def test_add_duplicate(self) -> None:
        self.assertTrue(self.trie.add("Apple"))
        self.assertFalse(self.trie.add("Apple"))


    # perhaps actually use root as empty str
    def test_add_blank(self) -> None:
        self.assertFalse(self.trie.add(""))


    def test_add_above_max_char(self) -> None:
        above_max = self.trie._max_depth + 1
        self.assertFalse(self.trie.add("i" * above_max))


    def test_add_with_space(self) -> None:
        self.assertTrue(self.trie.add("Apple Orchard"))


    def test_add_nad_char(self) -> None:
        self.assertFalse(self.trie.add("a+a"))


t = Trie()
# assert False


def test_contains() -> None:
    assert t.contains("Apple") == True
    assert not t.contains("Apples")
    assert not t.contains("App")
    assert not t.contains("ple")
    assert not t.contains("ppl")
    assert t.contains("AppleOrchard") == True
    assert t.contains("Apple Orchard") == True
    assert not t.contains("AppleOrchards")
    assert not t.contains("AppleOrchar")
    assert not t.contains("ppleOrchar")
    assert t.contains("Doggo") == True
    assert not t.contains("a+a")
    assert not t.contains("---")
    assert not t.contains("^asd")
    assert not t.contains("i" * 201)
    print("Contains tests passed!")


def test_get_all_words() -> None:
    assert t.get_all_words() == ['apple', 'appleorchard', 'apple orchard', 'doggo']
    print("Get_all_words tests passed!")


def test_get_suggestions() -> None:
    assert t.get_suggestions("app") == ['apple', 'appleorchard', 'apple orchard']
    assert t.get_suggestions("apple") == ['apple', 'appleorchard', 'apple orchard']
    assert t.get_suggestions("") == []
    assert t.get_suggestions("Steve") == []
    assert t.get_suggestions("a+a") == []
    assert t.get_suggestions("---") == []
    assert t.get_suggestions("^asd") == []
    print("Get suggestions tests passed!")


def test_delete() -> None:
    assert t.delete("AppleOrchard") == True
    assert not t.contains("AppleOrchard")
    assert not t.contains("AppleO")
    assert not t.contains("Appl")
    assert t.contains("Apple") == True
    assert t.contains("Doggo") == True
    assert not t.delete("Apples")
    assert t.contains("Apple") == True
    assert t.delete("Doggo") == True
    assert not t.contains("Doggo")
    assert t.contains("Apple")
    assert not t.delete("a+a")
    assert not t.delete("---")
    assert not t.delete("^asd")
    assert not t.delete("")
    print("Delete tests passed!")


if __name__ == "__main__":
    test_contains()
    test_get_all_words()
    test_get_suggestions()
    test_delete()

