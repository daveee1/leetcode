#made by chatgpt
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(start, cursum,curpair ):      
            if cursum==target:
                ans.append(list(curpair))     #dont use just ans.append(curpair): it would indicate a reference to curpair, we want a COPY of curpair
                return
            if cursum>target:
                return 
            for i in range (start, n):
                curpair.append(nums[i])
                backtrack(i, cursum+nums[i], curpair)    #we add nums[i] in the function so when we pop the latest value cursum remains the same from the beginning
                curpair.pop()
        n=len(nums)
        ans=[]
        backtrack(0,0,[])
        return ans
