class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n=len(digits)
        if n==0:
            return []
        def backtracking(index , currsol):        
            if index>n-1:
                m=len(currsol)
                s=""
                for i in range(m):
                    s+=str(currsol[i])
                ans.append(s)
                return
            m=len(alp_list[index])
            for i in range(m):
                currsol.append(alp_list[index][i])
                backtracking(index+1, currsol)
                currsol.pop()

        ans=[]
        alp_list=[]
        for  i in range(n):
            number=int(digits[i])
            if number<7:
                alp_list.append(list(map(chr, range(97+(number-2)*3,97+(number-2)*3+3))))
            else:
                if number==7:
                    alp_list.append(list(map(chr, range(ord('p'), ord('s')+1))))
                elif number==8:
                    alp_list.append(list(map(chr, range(ord('t'), ord('v')+1))))
                else:
                    alp_list.append(list(map(chr, range(ord('w'), ord('z')+1))))
        n=len(alp_list)
        backtracking(0,[])
        return ans
