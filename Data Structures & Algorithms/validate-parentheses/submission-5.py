class Solution:
    def isValid(self, s: str) -> bool:
        check = {'(' : ')', '[' : ']', '{' : '}'}
        stack = []
        for x in s:
            if x == '(' or x =='[' or x=='{':
                stack.append(x)
            else:
                if len(stack)>0 and  x == check[stack[-1]]:
                    stack.pop()
                else:
                    return False 
        if len(stack)==0:
            return True 
        else:
            return False
        