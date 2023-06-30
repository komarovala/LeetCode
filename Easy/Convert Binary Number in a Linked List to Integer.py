#https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data
class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def add_first(self, node):
        node.next = self.head
        self.head = node

ll = LinkedList()
#Создаем тестовый связный список
llist = LinkedList()
llist.head = Node(1)
llist.add_first(Node(0))
llist.add_first(Node(1))

print(ll)

nums = []

tmp = ll.head
while tmp:
    nums.append(tmp.data)
    tmp = tmp.next

print(nums)