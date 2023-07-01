def reverse_order(self, start, end):
    i = 0
    current_node = self.head
    while current_node is not None:
        if i == start - 1:
            start_front_node = current_node
            start_node = current_node.next
        elif i == 0 and start == 0:
            start_node = current_node
        elif i == end:
            end_node = current_node
            end_back_node = current_node.next

        current_node = current_node.next
        i += 1

    if i == end +1:
        self.tail = start_node

    first_node = start_node
    next_node = first_node.next
    for i in range(end-start):
        tmp_node = next_node.next
        next_node.next = first_node

        first_node = next_node
        next_node = tmp_node

    if start != 0:
        start_front_node.next = end_node
    else:
        self.head = end_node
    start_node.next = end_back_node