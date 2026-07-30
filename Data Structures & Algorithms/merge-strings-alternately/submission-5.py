class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s=''
        w_1 = 0
        w_2 = 0
        n = len(word1)
        m = len(word2)
        while w_1 < n and w_2 <m:
            s += word1[w_1] + word2[w_2]
            w_1+=1
            w_2+=1
        while w_1 < n :
            s+= word1[w_1]
            w_1+=1
        while w_2< m:
            s+=word2[w_2]
            w_2 +=1
        return s 
            