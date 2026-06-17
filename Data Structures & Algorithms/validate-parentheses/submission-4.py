class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = {')':'(','}':'{',']':'['}
        res = []
        for i in s:
            if i in parenthesis:
                if res and res[-1] == parenthesis[i]:
                    res.pop() 
                else:
                    return False
            else:
                res.append(i)
        return True if not res else False