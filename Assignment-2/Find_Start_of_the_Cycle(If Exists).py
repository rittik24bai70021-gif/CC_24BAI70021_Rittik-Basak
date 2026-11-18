# Find Start of the Cycle
# Floyd's Algorithm
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def detectCycle(head):

    slow = head
    fast = head

    while fast and fast.next:

        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break

    if not fast or not fast.next:
        return None

    slow = head

    while slow != fast:

        slow = slow.next
        fast = fast.next

    return slow

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

cycle_start = detectCycle(head)

if cycle_start:
    print("Output:", cycle_start.val)
    print("Cycle starts at node:", cycle_start.val)
else:
    print("Output: None")
    print("No cycle exists in the linked list.")