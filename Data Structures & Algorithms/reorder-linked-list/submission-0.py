# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev=None
        temp=slow.next
        slow.next=None
        while temp:
            temp2=temp.next
            temp.next=prev
            prev=temp
            temp=temp2
        temp=head
        while prev:
            temp2=temp.next
            prev2=prev.next
            temp.next=prev
            prev.next=temp2
            temp=temp2
            prev=prev2
        return None

        