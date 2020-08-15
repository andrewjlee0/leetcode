def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    int1 = ''
    while True:
        int1 += str(l1.val)
        if l1.next != None:
            l1 = l1.next
        else:
            break

    int2 = ''
    while True:
        int2 += str(l2.val)
        if l2.next != None:
            l2 = l2.next
        else:
            break

    summed = str(int(int1[::-1]) + int(int2[::-1]))
    print(int1, int2)

    sll = ListNode()
    old_node = None
    for i in summed:
        new_node = ListNode(i)
        new_node.next = old_node
        old_node = new_node

    return new_node
