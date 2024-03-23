class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        temp=nums[0]
        l=1
        max=temp
        while l<n:
            if nums[l]>=0:
                if temp<0:
                    temp=nums[l]
                else:
                    temp+=nums[l]
            else:
                if temp<nums[l]:
                    temp=nums[l]
                else:
                    temp+=nums[l]
            if temp>max:
                max=temp
            l+=1
        return max
