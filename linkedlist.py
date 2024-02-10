class Node:
    ''' Node class with an item and link that points to the next node '''
    def __init__(self, item: any, link =None) -> None:
        ''' Initialize the data and the link to the next node '''
        self.item = item
        self.link = link

    def __repr__(self) -> str:
        ''' Return a string representation of each node '''
        if self.link is None:
            return f"Node({self.item})"
        return f"Node ({self.item}) --> ({self.link})"

class LinkedList:
    ''' compiles the nodes into a linked list and adds functions to edit the nodes'''
    def __init__(self, items=None):
        ''' Initialize the 1st item in the linked list and the last '''
        self._head = None    # points to none to indicate LL is empty
        self._tail = None
        self._len = 0

        if items is not None:
            for item in items:
                self.add_last(item)
    
    def __len__(self):
        ''' keeps track of the length of the LL '''
        return self._len
    
    def __str__(self) -> str:
        current_node = self._head
        elements = []
        while current_node is not None:
            elements.append(str(current_node.item))
            current_node = current_node.link
        return " ".join(elements)
    
    def get_head(self):
        ''' keeps track of the 1st item in the LL '''
        if self._head is not None:
            return self._head.item
        else: return None

    def get_tail(self):
        ''' keeps track of the last item in the LL '''
        if self._tail is not None:
            return self._tail.item
        else: return None
    
    def add_first(self, item):
        ''' allows us to add to the beginning of the LL '''
        self._head = Node(item, self._head)
        if self._tail is None: self._tail = self._head
        self._len += 1

    def add_last(self, item):
        ''' allows us to add to the end of the LL '''
        if len(self) == 0:
            self.add_first(item)
        else:
            self._tail.link = Node(item)
            self._tail = self._tail.link
            self._len +=1

    def remove_last(self):
        ''' allows us to remove from the end of the LL ''' 
        # edge cases: if linkedlist len is 0 or 1
        if self._head is self._tail:
            return self.remove_first()

        penultimate = self._head
        while penultimate.link.link is not None:
            penultimate = penultimate.link
        item = penultimate.link.item
        penultimate.link = None
        self._tail = penultimate  # Update tail
        self._len -= 1
        return item

        

    def remove_first(self):
        ''' allows us to remove from the front of the LL '''  
        if self._head is None:
            raise RuntimeError('LL must not be empty')  
        item = self._head.item
        self._head = self._head.link
        if self._head is None: self._tail = None
        self._len -= 1
        return item
        
if __name__ == "__main__":
    ''' test case '''
    testLL = LinkedList()
    testLL.add_first(2)
    testLL.add_last(5)
    print(testLL)