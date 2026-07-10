# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length=0
        temp=head
        while temp:
            length+=1
            temp=temp.next
        ff=length-n
        if ff<1:
            return head.next
        prev=head
        temp=head.next
        while temp:
            if ff==1:
                prev.next=temp.next
                break
            temp=temp.next
            prev=prev.next
            ff-=1
        return head

        