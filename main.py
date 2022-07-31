from trie import Trie

SIZE_OF_CHAR_SET = 27

t = Trie(SIZE_OF_CHAR_SET)

t.add("Apple")
t.add("Apple")
t.add("AppleOrchard")
t.add("Doggo")
t.add("")
t.add("Apple Orchard")


def test_add_contains() -> None:
    # assert False
    assert t.contains("Apple")
    assert not t.contains("Apples")
    assert not t.contains("App")
    assert not t.contains("ple")
    assert not t.contains("ppl")
    assert t.contains("AppleOrchard")
    assert t.contains("Apple Orchard")
    assert not t.contains("AppleOrchards")
    assert not t.contains("AppleOrchar")
    assert not t.contains("ppleOrchar")
    assert t.contains("Doggo")
    print("Add and Contains tests passed!")


def test_get_all_words() -> None:
    assert t.get_all_words() == ['apple', 'appleorchard', 'apple orchard', 'doggo']
    print("Get_all_words tests passed!")


def test_get_suggestions() -> None:
    assert t.get_suggestions("app") == ['apple', 'appleorchard', 'apple orchard']
    assert t.get_suggestions("apple") == ['appleorchard', 'apple orchard']
    assert t.get_suggestions("") == ['apple', 'appleorchard', 'apple orchard', 'doggo']
    assert t.get_suggestions("Steve") == []
    print("Get suggestions tests passed!")


def test_delete() -> None:
    assert t.delete("AppleOrchard")
    assert not t.contains("AppleOrchard")
    assert not t.contains("AppleO")
    assert not t.contains("Appl")
    assert t.contains("Apple")
    assert t.contains("Doggo")
    assert not t.delete("Apples")
    assert t.contains("Apple")
    assert t.delete("Doggo")
    assert not t.contains("Doggo")
    assert t.contains("Apple")
    print("Delete tests passed!")


if __name__ == "__main__":
    test_add_contains()
    test_get_all_words()
    test_get_suggestions()

    test_delete()

