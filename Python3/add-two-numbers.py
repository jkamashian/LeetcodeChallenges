'''
https://leetcode.com/problems/add-two-numbers/
https://leetcode.com/problems/add-two-numbers/submissions/1214659502
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

 
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def add(l1: Optional[ListNode], l2: Optional[ListNode], remainder=0):
            output = ListNode()
            output.val = (l1.val + l2.val + remainder)  % 10
            remainder = (l1.val + l2.val + remainder)//10
            if(l1.next or l2.next or remainder):
                output.next = add(
                    l1 = l1.next if l1.next else ListNode(),
                    l2 = l2.next if l2.next else ListNode(),
                    remainder = remainder
                )
            return output
        return add(l1,l2, 0)
