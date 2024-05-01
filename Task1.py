class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def reverse_linked_list(head):
    previous = None
    current = head
    while current:
        next_node = current.next  # Збереження наступного вузла
        current.next = previous   # Реверсування посилання
        previous = current        # Переміщення previous на один вузол вперед
        current = next_node       # Переміщення current на один вузол вперед
    return previous  # Нова голова списку


def merge_sort(head):
    if not head or not head.next:
        return head
    
    # Розділення списку на дві половини
    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None
    
    left = merge_sort(head)
    right = merge_sort(next_to_middle)
    
    # Злиття двох відсортованих списків
    sorted_list = sorted_merge(left, right)
    return sorted_list

def get_middle(node):
    if not node:
        return node
    
    slow = node
    fast = node
    
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        
    return slow

def sorted_merge(a, b):
    if not a:
        return b
    if not b:
        return a
    
    if a.value <= b.value:
        result = a
        result.next = sorted_merge(a.next, b)
    else:
        result = b
        result.next = sorted_merge(a, b.next)
    return result


def merge_two_sorted_lists(l1, l2):
    dummy = ListNode()
    tail = dummy
    
    while l1 and l2:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
        
    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2
    
    return dummy.next
