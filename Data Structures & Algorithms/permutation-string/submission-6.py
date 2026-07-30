class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1)
        s_1 = {}
        s_2 = {}
        if len(s1) > len(s2):
            return False
        for x in s1:
            if x in s_1:
                s_1[x] +=1
            elif x not in s_1:
                s_1[x] = 1
        for y in range(len(s2)):
            if s2[y] in s_2:
                s_2[s2[y]] +=1
            else:
                s_2[s2[y]] = 1
            
            if y-l+1 > len(s1):
                s_2[s2[l]] -= 1
                if s_2[s2[l]] == 0:
                    del s_2[s2[l]]
                l += 1
            if y - l + 1 == len(s1):
                    if s_1 == s_2:
                        return True
        return False
                
        

