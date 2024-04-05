#Given a string s of lower and upper case English letters.

#A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

#0 <= i <= s.length - 2
#s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
#To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

#Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

#Notice that an empty string is also good




#chatgpt
    #class Solution:
#    def makeGood(self, s: str) -> str:
  #      stack = []
        
      #  for char in s:
        #    if stack and abs(ord(stack[-1]) - ord(char)) == 32:
         #       stack.pop()
          #  else:
           #     stack.append(char)
        
       # return ''.join(stack)


class Solution:
    def makeGood(self, s: str) -> str:
        n=len(s)
        if n==0 or n==1:
            return s
        i=0
        while i<len(s)-1:
            #check if one of the two is lower and the other upper
            #in that case break sin 3 parts : 
                #first part of the string from 0 to i-1
                #second is the two elements that will be substituted
                #third last part from i+2 to len(s)
            if s[i].isupper() and not s[i+1].isupper() and s[i]==s[i+1].upper():
                sfirst=s[:i]
                slast=s[i+2:]
                s=sfirst+slast
                i=-1
            elif not s[i].isupper() and s[i+1].isupper() and s[i]==s[i+1].lower():
                sfirst=s[:i]
                slast=s[i+2:]
                s=sfirst+slast
                i=-1
            i+=1
        return s
