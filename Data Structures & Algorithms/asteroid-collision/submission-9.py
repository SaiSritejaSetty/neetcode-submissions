class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for x in asteroids:
            while stack and x < 0 and stack[-1] > 0:
                if abs(x) > stack[-1]:
                    stack.pop()
                    
                elif abs(x) == stack[-1]:
                    stack.pop()
                    break
                elif abs(x) < stack[-1]:
                    break


            else:
                stack.append(x)
        return stack

        

                