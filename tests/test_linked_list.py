import pytest
from ..linked_list import Node, LinkedList


def test_Node_constructor():
    node = Node(3)

    assert node.data == 3
    assert node.prev is None
    assert node.next is None


def test_LinkedList_constructor():
    ll = LinkedList()
    assert ll.head is None
    assert ll.tail is None


def test_LinkedList_push_front():
    ll = LinkedList()
    ll.push_front(1)

    assert ll.head is ll.tail
    assert ll.head.data == 1

    ll.push_front(2)
    ll.push_front(3)

    assert ll.head.data == 3
    assert ll.head.next.data == 2
    assert ll.head.next.next.data == 1


def test_LinkedList_push_back():
    ll = LinkedList()
    ll.push_back(1)

    assert ll.head is ll.tail
    assert ll.head.data == 1

    ll.push_back(2)
    ll.push_back(3)

    assert ll.head.data == 1
    assert ll.head.next.data == 2
    assert ll.head.next.next.data == 3


def test_LinkedList_pop_front():
    ll = LinkedList()
    ll.push_back(1)
    ll.push_back(2)
    ll.push_back(3)

    assert ll.pop_front() == 1
    assert ll.head.data == 2
    assert ll.head.next.data == 3
    assert ll.head.next is ll.tail

    assert ll.pop_front() == 2
    assert ll.head.data == 3
    assert ll.head is ll.tail

    assert ll.pop_front() == 3
    assert ll.head is None

    with pytest.raises(IndexError):
        ll.pop_front()


def test_LinkedList_pop_back():
    ll = LinkedList()
    ll.push_back(1)
    ll.push_back(2)
    ll.push_back(3)

    assert ll.pop_back() == 3
    assert ll.head.data == 1
    assert ll.head.next.data == 2
    assert ll.head.next is ll.tail

    assert ll.pop_back() == 2
    assert ll.head.data == 1
    assert ll.head is ll.tail

    assert ll.pop_back() == 1
    assert ll.head is None

    with pytest.raises(IndexError):
        ll.pop_back()


def test_LinkedList_apply():
    ll = LinkedList()
    ll.push_back(1)
    ll.push_back(2)
    ll.push_back(3)

    power_fn = lambda x: x ** 2
    results = ll.apply(power_fn)

    assert results[0] == 1
    assert results[1] == 4
    assert results[2] == 9
