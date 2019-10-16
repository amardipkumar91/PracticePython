class ListNode:
    def __init__(self, node = None, next = None):
        self._node = node
        self._next = next
    
    def __repr__(self):
        return repr(self._node)
    
    def set_data(self, data):
        self._node = data
    
    def get_data(self):
        return self._node

    def set_next(self, next):
        self._next = next
    
    def get_next(self):
        return self._next
    
    def has_next(self):
        return self._next != None
    
class SinglyLinkList(object):
    def __init__(self, head = None):
        self.head = None
        self.length = 0

    def __repr__(self):
        nodes = []
        current = self.head
        while current: 
            nodes.append(repr(current))
            current = current.get_next()
        return '[' + ', '.join(nodes) + ']'

    def get_linklist_length(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
        return count

    def insert_data_at_beginning(self, data):
        new_node = ListNode()
        new_node.set_data(data)
        if self.length == 0:
            self.head = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node
        self.length += 1

obj = SinglyLinkList()
obj.insert_data_at_beginning('a')
obj.insert_data_at_beginning(23)
obj.insert_data_at_beginning(123)
print ("Link List is :--", obj)
print ("Length of linklist is :--", obj.get_linklist_length())


    