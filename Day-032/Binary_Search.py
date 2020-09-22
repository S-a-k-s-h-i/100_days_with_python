#ITERATIVE METHOD
# def bs(A,t):
#     st=0
#     end=len(A)-1
#     while st<=end:
#         m=(end+st)//2
#         if A[m]==t:
#             return m
#         elif A[m]>t:
#             end=m-1
#         else:
#             st=m+1
#     return -1

#RECURSIVE METHOD
def bs(A,t,st,end):
   if st<=end:
       m = (st + end) // 2
       if A[m] == t:
           return m
       elif t < A[m]:
           bs(A, t, st, m - 1)
       else:
           return bs(A,t,m+1,end)
   return -1
A=[int(x) for x in input().split()]
t=int(input())
st=0
end=len(A)-1
print(bs(A,t,st,end))