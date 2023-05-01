# https://leetcode.com/problems/merge-nodes-in-between-zeros/
#O(n^2)
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.val))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def add_first(self, node):
        node.next = self.head
        self.head = node
#Создаем тестовый связный список
llist = LinkedList()
llist.head = Node(0)
llist.add_first(Node(3))
llist.add_first(Node(1))
llist.add_first(Node(0))
llist.add_first(Node(4))
llist.add_first(Node(5))
llist.add_first(Node(0))
print(llist)

dummy = llist.head
tmp = llist.head.next  #т.к начинаем с нуля
sum = 0
while tmp:
    if tmp.val == 0:
        dummy = dummy.next
        dummy.val = sum
        sum = 0
    else:
        sum += tmp.val
    tmp = tmp.next
dummy.next = None

print(llist)

