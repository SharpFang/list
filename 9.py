class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def partition_list(head, x):
    dummy_less = ListNode(0)
    dummy_greater = ListNode(0)
    less, greater = dummy_less, dummy_greater

    while head:
        if head.val < x:
            less.next = head
            less = less.next
        else:
            greater.next = head
            greater = greater.next
        head = head.next

    greater.next = None
    less.next = dummy_greater.next

    return dummy_less.next

# Приклад
list_to_partition = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
partition_value = 3
partitioned_list = partition_list(list_to_partition, partition_value)

# Вивід результату
result = []
while partitioned_list:
    result.append(partitioned_list.val)
    partitioned_list = partitioned_list.next
print("Список після розділення за значенням", partition_value, ":", result)


