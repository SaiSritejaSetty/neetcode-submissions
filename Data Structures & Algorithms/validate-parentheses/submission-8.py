class Solution:
    def isValid(self, s: str) -> bool:
        curr = []
        check = {'(' : ')' , '{' : '}' , '[' : ']'}
        for x in s:
            if x in ('(', '{' , '['):
                curr.append(x)
            else:
                if len(curr) > 0 and x == check[curr[-1]]:
                    curr.pop()
                else:
                    return False
        if len(curr) == 0:
            return True
        
        return False
