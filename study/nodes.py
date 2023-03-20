class Box:
  def __init__ (self,data = None):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self, node):
    self.head = node

  def insert_at_beginning(self,node):
      node.next = self.head
      self.head = node
  def print_ll(self):
      s = ''
      tmp = self.head
      while tmp:
          s += str(tmp.data) + '->'
          tmp = tmp.next
      return s


ll = LinkedList(Box(1))
ll.insert_at_beginning(Box(2))

ll.insert_at_beginning(Box(3))

print(ll.head.data)

print(ll.print_ll())
