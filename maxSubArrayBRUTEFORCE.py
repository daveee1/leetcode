class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        f=0
        l=0
        max=nums[0]
        temp=0
        while f<n:
            temp=0
            l=f
            while l<n:
                temp+=nums[l]
                if max<temp:
                    max=temp
                l+=1
            f+=1
        return max
