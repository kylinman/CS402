class LinkedList:
    class Node:
        def __init__(self, val, next=None):
            self.val = val
            self.next = next

    def __init__(self):
        self.head = None

    def prepend(self, val):
        self.head = LinkedList.Node(val, self.head)

    def empty(self):
        return self.head is None

    def __iter__(self):
        p = self.head
        while p:
            yield p.val

            p = p.next

    def __repr__(self):
        return '[' + ', '.join(repr(x) for x in self) + ']'

    def delete_even(self):
        if self.head is None:
            return

        self.head = self.head.next
        current_node = self.head
        while current_node is not None and current_node.next is not None:
            current_node.next = current_node.next.next
            current_node = current_node.next