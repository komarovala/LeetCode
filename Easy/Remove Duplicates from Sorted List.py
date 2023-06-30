#https://leetcode.com/problems/remove-duplicates-from-sorted-list/
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_first(self, node):
        if self.tail is None:
            self.tail = node
        node.next = self.head
        if self.head is not None:
            self.head.prev = node
        self.head = node

    def add_tail(self, node):
        if self.head is None:
            self.head = node

        node.prev = self.tail
        if self.tail is not None:
            self.tail.next = node
        self.tail = node

    def delete(self, node):
        tmp = self.head

        while tmp:
            if tmp.val == node.val:
                if tmp.prev:
                    tmp.prev.next = tmp.next
                else:
                    self.head = tmp.next
            tmp = tmp.next
        return

    def insert(self, node_after, new_node):
        tmp = self.head
        while tmp is not None:
            if tmp.val == node_after.val:
                new_node.next = tmp.next
                new_node.prev = tmp
                tmp.next = new_node
                return
            tmp = tmp.next

    def insert_lst(self, node_after, new_list):
        pass

    def deleteDuplicates(self):
        tmp = self.head
        while tmp.next:
            if tmp.next.val == tmp.val:
                tmp.next = tmp.next.next
            else:
                continue
            tmp = tmp.next

    def print_ll(self):
        s = ''
        tmp = self.head
        while tmp:
            s += str(tmp.val) + '->'
            tmp = tmp.next
        return s


ll = LinkedList()
ll.add_first(Node(5))
ll.add_first(Node(1))
ll.add_first(Node(1))
ll.add_first(Node(4))
ll.add_first(Node(4))

ll.deleteDuplicates()

print(ll.print_ll())



