class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        if n==1:
            return [nums[0]]
        
        mf={}
        for  i in range(n):
            if nums[i] not in mf.keys():
                mf[nums[i]]=1
            else:
                mf[nums[i]]+=1
        
        l=[]
        max=-1
        key_for="-2w2222"
        
        for j in range(k):
            for key in mf.keys():
                if mf[key]>max:
                    max=mf[key]
                    keyfor=key
            l.append(keyfor)
            del mf[keyfor]         
            j+=1
            max=-1
        return l

        


