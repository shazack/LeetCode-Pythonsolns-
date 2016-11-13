# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0 
        temp = ListNode(0)
        result = temp
        if l1 is None and l2 is not None:
            return l2
        elif l2 is None and l1 is not None:
            return l1
        elif l1 is not None and l2 is not None:
            while l1 and l2:
                result.next = ListNode((l1.val+l2.val+carry)%10)
                carry = (l1.val+l2.val+carry)/10
                l1 = l1.next
                l2 = l2.next
                result = result.next
            if l1 is not None:
                while l1:
                    result.next = ListNode((l1.val+carry)%10)
                    carry = (l1.val+carry)/10
                    l1 = l1.next
                    result = result.next
            if l2 is not None:
                while l2:
                    result.next = ListNode((l2.val+carry)%10)
                    carry = (l2.val+carry)/10
                    l2 = l2.next
                    result = result.next
            if carry == 1:
                result.next = ListNode(1)
        return temp.next
            
                
                
                
                
            
            
        
