# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None


def add_head(arr: list):
    head = ListNode(arr[0])
    for i in arr[1:]:
        node = ListNode(i)
        node.next = head
        head = node
    return head


def reverse_node(head: ListNode) -> ListNode:
    """
    单向链表的反转：Input:1>2>3>4>5
                 Output:5>4>3>2>1

    思路：先将head.next断开，即指向断开的元素pre（none）;再将pre赋值head，将head赋值head.next;最后将head赋值pre
    :param head:ListNode
    :return:ListNode
    """
    if head is None:
        return head
    else:
        pre = None
        while head is not None:
            post = head.next
            head.next = pre
            pre = head
            head = post
        head = pre
        return head


def traversal(li: ListNode):
    if not li:
        return
    else:
        while li:
            print(li.val)
            li = li.next


list_node = add_head([1, 2, 3, 4, 5])
traversal(list_node)
reverse_list = reverse_node(list_node)
traversal(reverse_list)

