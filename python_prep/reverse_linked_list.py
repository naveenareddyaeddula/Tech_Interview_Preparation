class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

def traverse(head):
    curr = head
    while curr is not None:
        print(curr.data)
        curr = curr.next

print(traverse(head))

def rev(head):
    prev = None
    curr = head
    while curr:
        new_head = curr.next
        curr.next = prev
        prev = curr
        curr = new_head
    return prev
    
new_head = rev(head)
print(traverse(new_head))