class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        count = 0
        current = self.head 
        while current:
            if count == index:
                return current.val
            current = current.next
            count += 1
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head  # sets the next element of the new node to the current head
        if self.head:
            self.head.prev = new_node
        self.head = new_node  # sets new_node as the new head

    def addAtTail(self, val: int) -> None:
        new_tail = Node(val)
        if not self.head:  # if the list is empty
            self.head = new_tail
            return

        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_tail
        new_tail.prev = current

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        
        count = 0
        new_node = Node(val)
        current = self.head

        # Traverse to find the node before the index
        while current and count < index - 1:
            current = current.next
            count += 1

        # If current is None, the index is out of bounds
        if not current:
            return

        # Inserting the new node between current and current.next
        new_node.next = current.next
        if current.next:
            current.next.prev = new_node
        current.next = new_node
        new_node.prev = current

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or not self.head:
            return

        current = self.head
        if index == 0:  # Deleting the head node
            if self.head.next:
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head = None  # The list becomes empty
            return

        count = 0
        while current and count < index:
            current = current.next
            count += 1

        # If current is None, the index is out of bounds
        if not current:
            return

        # Update the pointers to delete the node at the given index
        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)