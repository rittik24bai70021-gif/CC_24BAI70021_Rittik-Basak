# Palindrome Linked List
# Optimized Approach: Reverse Second Half

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, curr = None, slow

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        second_head = prev

        p1, p2 = head, second_head

        result = True

        while p2:
            if p1.val != p2.val:
                result = False
                break

            p1 = p1.next
            p2 = p2.next

        return result

def createLinkedList(values):

    head = ListNode(values[0])
    current = head

    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next

    return head

values = list(
    map(int, input("Enter the linked list elements: ").split())
)

head = createLinkedList(values)

solution = Solution()
result = solution.isPalindrome(head)

print("Input:", values)

if result:
    print("Output: true")
    print("The linked list is a palindrome.")
else:
    print("Output: false")
    print("The linked list is not a palindrome.")