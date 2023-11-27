class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def double_linked_list(head):
    current = head
    carry = 0

    while current:
        current.val = current.val * 2 + carry
        carry, current.val = divmod(current.val, 10)
        if not current.next and carry:
            current.next = ListNode(carry)
            break
        current = current.next

    return head

# Приклад
number_to_double = ListNode(1, ListNode(8, ListNode(9)))
doubled_list = double_linked_list(number_to_double)

# Вивід результату
result = []
while doubled_list:
    result.append(doubled_list.val)
    doubled_list = doubled_list.next
print("Подвоєне число у вигляді зв’язаного списку:", result)
