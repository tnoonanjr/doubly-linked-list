import unittest
from linkedlist import Node, LinkedList

class TestNode(unittest.TestCase):
    ''' Tests the Node class'''
    def test_init(self):
        ''' tests the initization of the Node'''
        node1 = Node('hello', 'next')
        self.assertEqual(node1.item, 'hello')
        self.assertEqual(node1.link, 'next')

    def test_repr(self):
        ''' tests the representation of the Node'''
        node1 = Node(1, 2)
        self.assertEqual(repr(node1),  f"Node ({node1.item}) --> ({node1.link})")


class TestLinkedList(unittest.TestCase):     
    ''' Tests the LL class '''
    def test_len(self):
        ''' Tests the length of the linked list '''
        LL = LinkedList()
        self.assertEqual(LL._len, 0)
    
    def test_get(self):
        ''' Tests both get methods'''
        LL = LinkedList()
        LL.add_first(1)
        LL.add_first(2)
        self.assertEqual(LL.get_head(), 2)
        self.assertEqual(LL.get_tail(), 1)

    def test_add_first(self):
        ''' Tests the add_first method '''
        LL = LinkedList()
        LL.add_first(1)
        LL.add_first(2)
        LL.add_first(3)
        self.assertEqual(LL._head.item, 3)

    def test_add_last(self):
        ''' Tests the add_last method '''
        LL = LinkedList()
        LL.add_last(1)
        LL.add_last(2)
        LL.add_last(3)
        self.assertEqual(LL._tail.item, 3)

    def test_remove_first(self):
        ''' Tests the remove_first method '''
        LL = LinkedList()
        LL.add_last(2)
        LL.add_last(4)
        LL.add_last(6)
        LL.remove_first()
        self.assertEqual(LL._head.item, 4)

    def test_remove_last(self):
        ''' Tests the remove_last method '''
        LL = LinkedList()
        LL.add_last(1)
        LL.add_last(2)
        LL.add_last(3)
        LL.remove_last()
        self.assertEqual(LL._tail.item, 2)

    
if __name__ == "__main__":
    unittest.main()
