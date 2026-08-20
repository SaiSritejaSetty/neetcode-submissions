class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        number = 0
        people.sort()
        l = 0
        r=len(people)-1
        while l <= r:
            current = people[l] + people[r]
            if current <= limit:
                number += 1
                l +=1
                r -= 1
            elif current > limit:
                r-=1
                number +=1
        return number
        