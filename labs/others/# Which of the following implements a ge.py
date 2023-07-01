# Which of the following implements a generator-based iterator for a circular linked list, where self.head refers to the sentinel head?
yield self.head.next.val

n = self.head.next
while n:
    yield n.next.val



yield from self.head
while iter(self):
    yield n.val
    n = next(self)



n = self.head.next
while n is not self.head:
    yield n.val
    n =n.next
