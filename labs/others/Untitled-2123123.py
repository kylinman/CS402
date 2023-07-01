'''

linked List -->Problem :delete even 
Linked list 
Problem:delete even
Implement the sing


第三题的题目是 链表，问题是删除 
实现单项链表方法 delete_even  ，该方法从列表中删除偶值索引 （0，2，4... ）处所有元素

编程规则： 不能向类添加任何其他方法也不能调用其他方法 也不能使用任何其他的数据结构，例如列表和字典
'''

# start code

class LinkedList:
    class Node:
        def __init__(self, val, next=None):
            self.val = val
            self.next = next

    def __init__(self):
        self.head = None

    def prepend(self ,val):
        self.head = LinkedList.Node(val, self.head)

    def empty(self):
        return self.head is None

    def __iter__(self):
        p = self.head
        while p:
            yield p.val
            p = p.next
    
    def __reper__(self):
        return '['+ ','.join(repr(x) for x in self) + ']']

    def delete_even(self):
        # your code