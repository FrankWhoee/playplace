class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    curr = head
    length = 0
    while curr is not None:
        length += 1
        curr = curr.next
    curr = head
    i = 0
    while i < length - n - 1:
        curr = curr.next
        i += 1
    if curr.next is None:
        head = None
    else:
        curr.next = curr.next.next
    return head

inp = ListNode(val=1, next=ListNode(val=2))
outp = removeNthFromEnd(inp,2)
print(outp.val)