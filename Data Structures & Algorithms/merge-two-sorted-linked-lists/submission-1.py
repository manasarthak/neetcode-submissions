# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1,temp2=head1,head2
        final_head=ListNode(-101,None)
        temp3=final_head
        while temp1 and temp2:
            if temp1.val<=temp2.val:
                temp3.next=temp1
                temp1=temp1.next
            else:
                temp3.next=temp2
                temp2=temp2.next
            temp3=temp3.next
        if temp1:
            temp3.next=temp1
        if temp2:
            temp3.next=temp2
        return final_head.next




        