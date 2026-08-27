class Solution:
    def decodeString(self, s: str) -> str:
            res = ""
            stack = []
            for x in s:
                if x.isalpha() or x.isdigit() or x == '[':
                    stack.append(x)
                elif x == ']':
                    temp = ''
                    while stack[-1] != '[':
                        temp = stack.pop() + temp
                    stack.pop()

                    num = ''
                    while stack and stack[-1].isdigit():
                        num = stack.pop() + num
                    number = int(num)

                    stack.append(temp * number)
            return "".join(stack)
                         


                    