#not correct for k=5k
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        n=len(nums)
        if k==n:
            return [max(nums)]
        subnum=[]
        lista=[]
        first=0
        last=k
        while last<n+1:
            subnum=nums[first:last]
            mmm=max(subnum)
            lista.append(mmm)
            first+=1
            last+=1
        return lista
