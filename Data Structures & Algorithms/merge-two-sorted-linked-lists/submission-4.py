# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_linked_list = ListNode()
        head = new_linked_list
        l_1 = []
        if not list1 and not list2:
            return 
        while list1 != None:
            l_1.append(list1.val)
            list1 = list1.next
        l_2 = []
        while list2 != None:
            l_2.append(list2.val)
            list2 = list2.next
        i = 0
        l = sorted(l_1+l_2)
        print(l)
        for i in range(len(l)):
            new_linked_list.val = l[i]
            if i < len(l) - 1:
                new_linked_list.next = ListNode()
                new_linked_list = new_linked_list.next
            i+=1
        return head
