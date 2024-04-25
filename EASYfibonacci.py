class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        list=[-1]*(n+1)
        list[0]=0
        list[1]=1
        return self.f(n,list)
    
    def f(self,n,list):
        if list[n]==-1:
            list[n]=self.f(n-1,list)+self.f(n-2,list)
        return list[n]
