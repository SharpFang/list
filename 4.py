class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorder_list(head):
    if not head or not head.next:
        return head

    # Знаходження середини списку
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Реверс другої половини списку
    second_half = slow.next
    slow.next = None
    prev = None
    while second_half:
        temp = second_half.next
        second_half.next = prev
        prev = second_half
        second_half = temp

    # Злиття двох відсортованих списків
    first_half = head
    second_half = prev
    while second_half:
        temp1, temp2 = first_half.next, second_half.next
        first_half.next = second_half
        second_half.next = temp1
        first_half, second_half = temp1, temp2

    return head

# Приклад
list_to_reorder = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
reordered_list = reorder_list(list_to_reorder)

# Вивід результату
result = []
while reordered_list:
    result.append(reordered_list.val)
    reordered_list = reordered_list.next
print("Перевпорядкований список:", result)
