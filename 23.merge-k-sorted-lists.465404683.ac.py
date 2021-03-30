# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        sortedList = []
        sortedVal = []
        for l in lists:
            while l:
                sortedList.append(l)
                sortedVal.append(l.val)
                l = l.next
        sortedVal.sort()
        for i in xrange(len(sortedVal)):
            sortedList[i].val = sortedVal[i]
            if i > 0:
                sortedList[i-1].next = sortedList[i]
        return sortedList[0] if sortedList else None
