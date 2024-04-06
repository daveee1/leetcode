#helped by chatgpt: very useful pop and the logic behind it simple but effective

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        stackelimination=[]
        n=len(s)
        for i in range(n):
            if s[i]=="(":
                stack.append(i)
            elif s[i]==")":
                if stack:
                    stack.pop()
                else :
                    stackelimination.append(i)
        
        #considering opened but not closed parenthesis
        for i in stack:
            stackelimination.append(i)
        print(stackelimination)
        #eliminate everything in stackelimination
        list=[]
        for i in range(n):
            if i not in stackelimination:
                list.append(s[i])
        

        return list
