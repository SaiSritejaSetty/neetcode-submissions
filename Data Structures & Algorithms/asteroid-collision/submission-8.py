class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for x in asteroids:
            while stack and x < 0 and stack[-1] > 0:
                diff = stack[-1] + x
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    break
                elif diff == 0:
                    stack.pop()
                    break
            else:
                stack.append(x)
            
            
        return stack

                