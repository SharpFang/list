class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(list1, list2):
    dummy = ListNode()
    current = dummy

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    if list1:
        current.next = list1
    elif list2:
        current.next = list2

    return dummy.next

# Приклад
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
merged_list = merge_two_lists(list1, list2)

# Вивід результату
result = []
while merged_list:
    result.append(merged_list.val)
    merged_list = merged_list.next
print("Об'єднані два відсортовані списки:", result)
