class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums=sorted(nums)
        massimo=1
        count=1

        for i in range(len(nums)-1):
            if nums[i]+1==nums[i+1]:
                count=count+1
                if count>massimo:
                    massimo=count
            elif nums[i]==nums[i+1]:
                #count remains equal
                count=count

            else:
                count=1
        return massimo
