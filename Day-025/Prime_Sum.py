class Solution:
    # @param A : integer
    # @return a list of integers
    def Prime(self,num):
        if num>1:
          for i in range(2,num):
            if num%i==0:
                return False
          else:
            return True
    def primesum(self, A):
        for i in range(2,A):
            if self.Prime(i):
               if self.Prime(A-i):
                  return [i,A-i]
