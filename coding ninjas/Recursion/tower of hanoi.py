# def tower_hanoi(n,a,b,c):
    # if n==1:
#         print('move 1st disk from', a, 'to',c)
#         return
#     tower_hanoi(n-1,a,c,b)
#     print('move',n,'th disk from',a,'to',c)
#     tower_hanoi(n-1,b,a,c)


# tower_hanoi(3,'a','b','c')


class Solution:
    
    def toh(self, N, fromm, to, aux):
        # Your code here
        if N==0:
            return
        Solution.toh(self,N-1,fromm,aux,to)
        print("move disk",N, "from rod", fromm, "to rod", to)
        Solution.toh(self, N-1,aux,to,fromm)
        return 2**N-1
        print(count="2**N-1") 

x=Solution()
print(x.toh(2,1,3,2))