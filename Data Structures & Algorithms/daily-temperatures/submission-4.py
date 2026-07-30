class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for x in range(len(temperatures)):
            l = x+1
            while l < len(temperatures):
                if temperatures[x] >= temperatures[l]:
                    l+=1
                elif temperatures[x] < temperatures[l]:
                    diff = l - x
                    res.append(diff)
                    break
            else:
                res.append(0)
        return res 

        