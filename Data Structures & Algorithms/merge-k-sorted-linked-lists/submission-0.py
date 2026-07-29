# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #edge case
        if not lists:
            return None
        # merge two lists
        # 0 and 1 -> 0
        # 2 and 3 -> 2
        # 4 and 5 -> 4

        # then merge
        # 0 and 2 --> 0
        # 4 and .. if exists

        # then merge
        # 0 and 4

        interval = 1
        while interval < len(lists):
            i = 0
            while i + interval < len(lists):
                lists[i] = self.merge2Lists(lists[i], lists[i+interval])
                i += interval*2
            interval *=2 
        return lists[0]




    # look at two lists at a time
    # [1, 2, 4]
    # [1, 3, 5]

    # compare 0th index with 0th index 
    # if list a 0th index is < = list b 0th index 
    # add list a's 0th index and then move pointer of list a

    def merge2Lists(self, lista: Optional[ListNode], listb: Optional[ListNode]) -> Optional[ListNode]:
       
        # create a new list
        head = ListNode(0)
        # [0, merged list here]
        curr = head

        # repeat while they are still there
        while lista and listb:
            if lista.val <= listb.val:
                curr.next = lista
                lista = lista.next
            else:
                curr.next = listb
                listb = listb.next
            curr = curr.next
        if lista:
            curr.next = lista
        elif listb:
            curr.next = listb
        
        return head.next






