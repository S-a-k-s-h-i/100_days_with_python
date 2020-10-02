class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def getIntersectionNode(self, A, B):
        F = A
        G = B
        while F != G:
            if F == None:
                F = B
            else:
                F = F.next
            if G == None:
                G = A
            else:
                G = G.next
        return F