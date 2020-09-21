class Solution:
    def hammingDistance(self, A):
        answer=0
        for i in range(32):
            count=0
            for j in range(len(A)):
               if A[j] & (1<<i):
                   count+=1
            answer+=2*count*(len(A)-count)
        answer=answer%1000000007
        return answer
