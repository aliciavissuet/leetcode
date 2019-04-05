def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = 0
        pointer1 = head
        pointer2 = head

        while pointer1:
            length += 1
            pointer1 = pointer1.next
        if length-n-1 > 0:
            for i in range(length-n-1):
                pointer2 = pointer2.next
            if pointer2.next != None:
                pointer2.next = pointer2.next.next
        elif length == 1:
            return []
        elif length-n-1 == -1:
            head = head.next
        elif length-n-1 == 0:
            head.next = head.next.next

        return head
