class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        values = []
        for x in range(len(tokens)):
            if tokens[x] =='+':
                a = values.pop()
                b = values.pop()
                values.append(a+b)
            elif tokens[x] == "-":
                a = values.pop()
                b = values.pop()
                values.append(b-a)
            elif tokens[x] == "*":
                a = values.pop()
                b = values.pop()
                values.append(a*b)
            elif tokens[x] == "/":
                a = values.pop()
                b = values.pop()
                values.append(int(b/a))
            else:
                values.append(int(tokens[x]))

        res = values[0]
        return res   