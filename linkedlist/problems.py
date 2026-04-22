
# LINKED LIST Complete Implementation
# Topics: SLL Insert, Delete, Traverse, Search

# SINGLY LINKED LIST

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


#TRAVERSAL

def traverse(head):
    curr = head
    while curr.next is not None:
        print(curr.data, end=" -> ")
        curr = curr.next
    


# INSERTION 

def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    head=new_node


def insert_at_end(head, data):
    new_node = Node(data)
    if head is None:
        return new_node
    curr = head
    while curr.next is not None:
        curr = curr.next
    curr.next = new_node
    return head


def insert_at_kth(head, data, k):
    new_node = Node(data)
    if k == 0:
        new_node.next = head
        head=new_node
    curr = head
    for i in range(k-1):
        if curr is None:
            raise IndexError("Index out of range")
        curr = curr.next
    new_node.next = curr.next
    curr.next = new_node
    return head


# DELETION 

def delete_head(head):
    
    if head is None:
        return None
    return head.next


def delete_tail(head):
    
    if head is None or head.next is None:
        return None
    curr = head
    while curr.next.next is not None:
        curr = curr.next
    curr.next = None
    return head


def delete_at_kth(head, k):
    
    if head is None:
        return None
    if k == 0:
        return head.next
    curr = head
    for i in range(k - 1):
        if curr.next is None:
            raise IndexError("Index out of range")
        curr = curr.next
    curr.next = curr.next.next
    return head


# SEARCH 

def find_min(head):
    if head is None:
        return None
    min_val = head.data
    curr = head.next
    while curr is not None:
        if curr.data < min_val:
            min_val = curr.data
        curr = curr.next
    return min_val


def find_max(head):
    if head is None:
        return None
    max_val = head.data
    curr = head.next
    while curr is not None:
        if curr.data > max_val:
            max_val = curr.data
        curr = curr.next
    return max_val


def find_middle(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


