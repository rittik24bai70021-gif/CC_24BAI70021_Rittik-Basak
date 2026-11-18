# Palindrome Linked List - Brute Force

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createLinkedList(values):
    head = ListNode(values[0])
    current = head

    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next

    return head

def isPalindrome(head):
    values = []

    current = head

    while current:
        values.append(current.val)
        current = current.next

    left = 0
    right = len(values) - 1

    while left < right:
        if values[left] != values[right]:
            return False

        left += 1
        right -= 1

    return True

values = list(map(int, input("Enter the linked list elements: ").split()))

head = createLinkedList(values)
result = isPalindrome(head)

print("Input:", values)

if result:
    print("Output: true")
    print("The linked list is a palindrome.")
else:
    print("Output: false")
    print("The linked list is not a palindrome.")