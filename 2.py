class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_duplicates(head):
    current = head

    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next

    return head

# Приклад
sorted_list_with_duplicates = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
unique_list = remove_duplicates(sorted_list_with_duplicates)

# Вивід результату
result = []
while unique_list:
    result.append(unique_list.val)
    unique_list = unique_list.next
print("Список без дублікатів:", result)
