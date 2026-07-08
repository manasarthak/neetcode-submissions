# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        left=None
        while temp:
            temp2=temp.next
            temp.next=left
            left=temp
            temp=temp2
        return left
        

       
