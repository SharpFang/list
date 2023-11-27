class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

# Приклад
cyclic_list = ListNode(3, ListNode(2, ListNode(0, ListNode(-4))))
cyclic_list.next.next.next.next = cyclic_list.next
has_cycle_result = has_cycle(cyclic_list)
print("Наявність циклу у списку:", has_cycle_result)
