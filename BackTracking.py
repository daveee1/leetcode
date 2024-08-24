def function(nums):
  def backtracking(start,curpair):
    #case base
    if True:
      ans.append(list(curpair))
    #recursion
    for i in range(n):
      curpair.append(nums[i])
      backtracking(i+1, curpair)
      curpair.pop()

  n=len(nums)
  ans=[]
  backtracking(0,[])
  return ans
