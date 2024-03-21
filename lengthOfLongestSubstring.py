class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        massimo=0
        count=0
        first=0
        last=0
        lista=[]
        while last<len(s):
            if s[last] not in lista:
                lista.append(s[last])
                count+=1
                last+=1
            else:
                print(s[last])
                massimo=max(count,massimo)
                count=0
                first+=1
                last=first
                lista=[]
        #ultimi char
        massimo=max(count,massimo)
        
        return massimo
