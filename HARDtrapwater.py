class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        if n==1:
            return 0
        water=0
        f=0
        l=1
        maxtemp=max(height[1:])
        while f<n-1:
            #check if height[f] < to at least one of the heights
            maxtemp=max(height[f+1:])
            print(height[f],maxtemp)
            if height[f]==0: 
                f+=1
                l=f+1
            elif  height[f]>maxtemp:
                height[f]=maxtemp
            elif height[f]>height[l]:
                print("entrato  ",height[f],height[l])
                water+=height[f]-height[l]
                l+=1
            else:
                f=l
                l+=1
        return water
