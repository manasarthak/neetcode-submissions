class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        # 1. weave
        temp = head
        while temp:
            temp.next = Node(temp.val, temp.next, None)
            temp = temp.next.next

        # 2. randoms (must not touch .next here)
        temp = head
        while temp:
            temp.next.random = temp.random.next if temp.random else None
            temp = temp.next.next

        # 3. unweave + restore
        temp = head
        dummy = ans = Node(0)
        while temp:
            copy = temp.next
            temp.next = copy.next
            ans.next = copy
            ans = copy
            temp = temp.next
        return dummy.next