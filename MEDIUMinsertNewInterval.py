class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        list=[]
        for interval in intervals:
            if newInterval[1]<interval[0]:
                break
            else:
                if newInterval[0]>interval[1]:
                    list.append(interval)
                elif newInterval[0]>interval[0]:
                    #in this case newI wins so newInterval[0] is agglomerated in interval, so... 
                    newInterval[0]=interval[0]       
                    if interval[1]>newInterval[1]:
                        newInterval[1]=interval[1] 
                elif newInterval[1]==interval[0]:
                    newInterval[1]=interval[1]
                elif newInterval[1]<interval[1]:
                    newInterval[1]=interval[1]
                #i checked and agglomerated the current interval in newInterval
        list.append(newInterval)
        
        
        #copy all the rest
        for interval in intervals:
            if interval[0]>newInterval[1]:
                list.append(interval)

        return list
