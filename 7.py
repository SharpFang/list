from heapq import heappush, heappop

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_sorted_lists(lists):
    min_heap = []

    for i, lst in enumerate(lists):
        if lst:
            heappush(min_heap, (lst.val, i, lst))

    dummy = ListNode()
    current = dummy

    while min_heap:
        _, index, node = heappop(min_heap)
        current.next = node
        current = current.next

        if node.next:
            heappush(min_heap, (node.next.val, index, node.next))

    return dummy.next

# Приклад
lists_to_merge = [
    ListNode(1, ListNode(4, ListNode(5))),
    ListNode(1, ListNode(3, ListNode(4))),
    ListNode(2, ListNode(6))
]
merged_list = merge_k_sorted_lists(lists_to_merge)

# Вивід результату
result = []
while merged_list:
    result.append(merged_list.val)
    merged_list = merged_list.next
print("Об'єднаний відсортований список:", result)