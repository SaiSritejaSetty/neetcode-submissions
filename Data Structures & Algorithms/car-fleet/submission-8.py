class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = sorted(zip(position, speed), reverse = True)
        time = []
        res = 0
        for p , s in pair:
            t = (target - p) / s
            if time and t <= time[-1]:
                pass
            else:
                time.append(t)
                res+=1
        return res 
            


            
        