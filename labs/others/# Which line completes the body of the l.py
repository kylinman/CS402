# Which line completes the body of the loop in the following method so that it correctly reverses the order of the nodes in the underlying doubly-linked list (with a sentinel head node)?

def reverse(self):
    self.head.next, self.head.prior = self.head.prior , self.head.next
    n = self.head.next
    while n is not self.head:

        ____________________________________
        n = n.next

