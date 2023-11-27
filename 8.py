class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def reverse_k_group(head, k):
    def reverse_list(start, end):
        prev, current = None, start

        while current != end:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        return prev

    dummy = ListNode(0)
    dummy.next = head
    current, prev = head, dummy

    while current:
        group_start, group_end = current, current

        # Знаходження кінця групи
        for _ in range(k):
            if not group_end:
                break
            group_end = group_end.next

        if group_end:
            next_group_start = group_end.next
            reversed_group_start = reverse_list(group_start, group_end)
            prev.next = reversed_group_start
            group_start.next = next_group_start
            prev = group_start
            current = next_group_start
        else:
            break

    return dummy.next

# Приклад
list_to_reverse = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k_value = 2
reversed_list = reverse_k_group(list_to_reverse, k_value)

# Вивід результату
result = []
while reversed_list:
    result.append(reversed_list.val)
    reversed_list = reversed_list.next
print("Розвернуті вузли у групах по", k_value, ":", result)

