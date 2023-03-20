# https://leetcode.com/problems/merge-nodes-in-between-zeros/
#O(n^2)
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return self.val

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
llist.add_first(Node(0))
print(llist)

cnt = 0
nums = []
head = llist.head
while head:
    if head.val != 0:
        cnt += head.val
    else:
        nums.append(cnt)
        cnt = 0
    head = head.next

ll = LinkedList()

for i in nums:
    if i == 0:
        continue
    else:
        ll.add_first(Node(i))
print(ll)