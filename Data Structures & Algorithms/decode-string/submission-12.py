class Solution:
    def decodeString(self, s: str) -> str:
            stack = []
            curr = ''
            num = ''
            for x in s:
                if x.isdigit() or x.isalpha() or x == "[":
                    stack.append(x)
                elif x=="]":
                    while stack[-1] != "[":
                        curr = stack.pop() + curr
                    stack.pop()
                    while stack and stack[-1].isnumeric():
                        num = stack.pop() + num
                    curr = int(num)*curr
                    num = ''
                    stack.append(curr)
                    curr = ''
            return ''.join(stack)

                    