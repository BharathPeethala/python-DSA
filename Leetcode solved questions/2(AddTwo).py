class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        head = ListNode()
        while(l1 and l2):
            newNode = ListNode()
            if l1.val+l2.val+carry > 9:
                newNode.val = (l1.val+l2.val+carry) % 10
                carry = 1
            else:
                newNode.val = (l1.val+l2.val+carry) % 10
                carry = 0
            newNode.next = head.next
            head.next = newNode
            l1 = l1.next
            l2 = l2.next
        while(l1):
            newNode = ListNode()
            if l1.val+carry > 9:
                newNode.val = (l1.val+carry) % 10
                carry = 1
            else:
                newNode.val = (l1.val+carry) % 10
                carry = 0
            newNode.next = head.next
            head.next = newNode
            l1 = l1.next
        while(l2):
            newNode = ListNode()
            if l2.val+carry > 9:
                newNode.val = (l2.val+carry) % 10
                carry = 1
            else:
                newNode.val = (l2.val+carry) % 10
                carry = 0
            newNode.next = head.next
            head.next = newNode
            l2 = l2.next
        if carry:
            newNode = ListNode(carry)
            newNode.next = head.next
            head.next = newNode
        prev = None
        current = head.next
        while(current):
            next1 = current.next
            current.next = prev
            prev = current
            current = next1
        return prev
