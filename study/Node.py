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
        while tmp is not None:
            if tmp.next.val == node.val:
                tmp.next = tmp.next.next
                return
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

    def print_ll(self):
        s = ''
        tmp = self.head
        while tmp:
            s += str(tmp.val) + '->'
            tmp = tmp.next
        return s


ll = LinkedList()
# print(Node(1).val, Node(1).next)
ll.add_first(Node(2))
ll.add_first(Node(5))
ll.add_first(Node(4))
ll.add_first(Node(1))
ll.add_first(Node(6))

print(ll.print_ll())

# ll.delete(Node(5))
# print(ll.print_ll())
#
ll.insert(Node(5), Node(7))
print(ll.print_ll())