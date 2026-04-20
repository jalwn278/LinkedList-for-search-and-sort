import pytest
import sys
import os
from project import LinkedList, main, convert, Node

def test_node():
    node = Node()
    assert node.next == None

def test_llappend():
    ll = LinkedList()
    ll.append(("1", "Alice"))
    ll.append(("2", "Bob"))
    assert ll.head.data == ("2", "Bob")
    assert ll.head.next.data == ("1", "Alice")

def test_bubble():
    ll = LinkedList()
    ll.append(("3", "C"))
    ll.append(("1", "A"))
    ll.append(("2", "B"))

    ll.Bubble()
    assert ll.head == ("1", "A")
    assert ll.head.next.data == ("2", "B")

def test_merge():
    ll = LinkedList()
    ll.append(("10", "Zoe"))
    ll.append(("01", "Abby"))
    ll.Merge()
    assert ll.head.data == ("01", "Abby")

def test_selection():
    ll = LinkedList()
    ll.append(("3", "C"))
    ll.append(("1", "A"))
    ll.append(("2", "B"))

    ll.Bubble()
    assert ll.head == ("1", "A")

def test_linearsearch():
    ll = LinkedList()
    ll.append(("3", "C"))
    ll.append(("1", "A"))
    ll.append(("2", "B"))

    ll.Linear()
    assert "('3', 'C') is here" in ll.Linear("C")
    assert ll.Linear("4") == "Doesn't found"

def test_help(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["project.py", "-h"])
    with pytest.raises(SystemExit) as e:
        main()
    assert "This module support" in e.value.code

def test_length(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["project.py", "one argument"])
    with pytest.raises(SystemExit) as e:
        main()
    assert e.value.code == "It's too long so too short"

def test_extension(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["project.py", "data.png", "-Bubble"])
    with pytest.raises(SystemExit) as e:
        main()
    assert "eg: xxx.py .csv/.txt" in e.value.code

def test_input(monkeypatch):
    ll = LinkedList()
    ll.append(("1", "p"))
    monkeypatch.setattr("builtins.input", lambda _: "1")

    result = ll.Binary("1")
    assert ("1", "p") in result

def test_txt(tmp_path, monkeypatch):
    d = tmp_path / "test_dir"
    d.mkdir()
    file_path = d / "data.txt"
    file_path.write_text("101 Alice\n102 Bob")

    monkeypatch.setattr(sys, "argv", ["project.py", str(file_path), "-Bubble"])
    convert(".txt")

def test_csv(tmp_path, monkeypatch):
    d = tmp_path / "test_dir_csv"
    d.mkdir()
    file_path = d / "data.csv"
    file_path.write_text("id,name\n1,Alice\n2,Bob")

    monkeypatch.setattr(sys, "argv", ["project.py", str(file_path), "-Bubble"])
    convert(".csv")

def test_format(tmp_path, monkeypatch):
    file_path = tmp_path / "bad.txt"
    file_path.write_text("101 Alice extra_data")

    monkeypatch.setattr(sys, "argv", ["project.py", str(file_path), "-Bubble"])
    with pytest.raises(SystemExit) as e:
        convert(".txt")
    assert "Library only support One-One relations" in e.value.code