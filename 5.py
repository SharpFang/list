class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete_node(node):
    if not node or not node.next:
        return

    next_node = node.next
    node.val = next_node.val
    node.next = next_node.next

# Приклад
list1 = ListNode(4, ListNode(5, ListNode(1, ListNode(9))))
node_to_delete = list1.next  # Видаляємо вузол зі значенням 5
delete_node(node_to_delete)

# Вивід результату
result = []
while list1:
    result.append(list1.val)
    list1 = list1.next
print("Список після видалення вузла:", result)
