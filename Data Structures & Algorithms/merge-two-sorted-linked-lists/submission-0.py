# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedList = ListNode(-1)
        tempMerged = mergedList
        currList1 = list1
        currList2 = list2
        while currList1 and currList2:
            if currList1.val < currList2.val:
                tempMerged.next = currList1
                currList1 = currList1.next
                tempMerged = tempMerged.next
            else:
                tempMerged.next = currList2
                currList2 = currList2.next
                tempMerged = tempMerged.next
        if currList1:
            tempMerged.next = currList1
        if currList2:
            tempMerged.next = currList2
        return mergedList.next 
        