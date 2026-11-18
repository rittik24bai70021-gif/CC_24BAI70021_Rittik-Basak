class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def oddEvenList(head):
    if head is None or head.next is None:
        return head

    odd = head
    even = head.next
    evenHead = even

    while even is not None and even.next is not None:
        odd.next = even.next
        odd = odd.next

        even.next = odd.next
        even = even.next

    odd.next = evenHead

    return head


# Taking input from user
values = list(map(int, input("Enter linked list elements: ").split()))

# Creating the linked list
head = None
tail = None

for value in values:
    newNode = ListNode(value)

    if head is None:
        head = newNode
        tail = newNode
    else:
        tail.next = newNode
        tail = newNode


# Apply Odd-Even Linked List
res = oddEvenList(head)

# Display the result
print("Odd-Even Linked List:", end=" ")

while res is not None:
    print(res.val, end=" ")
    res = res.next