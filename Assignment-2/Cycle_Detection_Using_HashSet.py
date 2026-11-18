# Cycle Detection using HashSet

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def hasCycle(head):

    visited = set()

    current = head

    while current:

        if current in visited:
            return True
        visited.add(current)

        current = current.next

    return False

def createLinkedList(values):

    head = ListNode(values[0])
    current = head

    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next

    return head

values = list(
    map(int, input("Enter linked list elements: ").split())
)


head = createLinkedList(values)


pos = int(input("Enter cycle position (-1 for no cycle): "))

if pos != -1:

    cycle_node = head
    tail = head

    for i in range(pos):
        cycle_node = cycle_node.next

    while tail.next:
        tail = tail.next

    tail.next = cycle_node


result = hasCycle(head)

if result:
    print("Output: true")
    print("Cycle exists in the linked list.")
else:
    print("Output: false")
    print("No cycle exists in the linked list.")