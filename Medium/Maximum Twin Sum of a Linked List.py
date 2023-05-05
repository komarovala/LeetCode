#https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
from study.Node import Node, LinkedList

ll = LinkedList()
ll.add_first(Node(1))
ll.add_first(Node(2))
ll.add_first(Node(4))
ll.add_first(Node(5))


def pairSum(ll) -> int:
    d = {}
    i = 0
    tmp = ll.head
    while tmp:
        d[i] = tmp.val
        i += 1
        tmp = tmp.next

    n = len(d)
    maximum = 0

    for i in range(n - 1):
        ind = n - 1 - i
        if maximum < (d[i] + d[ind]):
            maximum = d[i] + d[ind]
    return maximum

print(pairSum(ll))


