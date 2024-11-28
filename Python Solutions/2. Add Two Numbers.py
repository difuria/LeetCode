# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list_1 = []
        while l1 != None:
            list_1.append(l1.val)
            l1 = l1.next

        list_2 = []
        while l2 != None:
            list_2.append(l2.val)
            l2 = l2.next
        print(list_1, list_2)
        
        int_1 = int("".join((list(map(str, list_1[::-1])))))
        int_2 = int("".join((list(map(str, list_2[::-1])))))

        arr = list(map(int, list(str(int_1 + int_2))))[::-1]

        new_node = ListNode(arr[0])
        adding_node = new_node
        for i in arr[1:]:
            current_node = ListNode(i)
            adding_node.next = current_node
            adding_node = adding_node.next
        return new_node
