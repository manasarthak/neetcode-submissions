# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans=temp=ListNode()
        while True:
            append=float('inf')
            pos=-1
            for i,head in enumerate(lists):
                if head and head.val<append:
                    append=head.val
                    pos=i
            if pos==-1:
                break
            temp.next=lists[pos]
            temp=temp.next
            lists[pos]=lists[pos].next
        return ans.next