class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        #now the alg is O(n) if and only if the sorted alg is O(n): not possible, i think the alg is O(nlogn)
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
