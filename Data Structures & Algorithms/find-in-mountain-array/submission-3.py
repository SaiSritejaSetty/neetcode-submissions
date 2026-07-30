class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l = 0
        r = mountainArr.length()-1
        while l < r:
            k = (l + r) // 2
            if mountainArr.get(k) < mountainArr.get(k+1):
                l = k + 1
            else:
                r = k
        peak = l     
        high = peak
        low = 0
        while low <= high:
            mid = (high+low) // 2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val>target:
                high = mid -1
            elif val<target:
                low = mid + 1
        high1 = mountainArr.length()-1
        low1= peak+1
        while low1<=high1:
            midd = (high1+low1)//2
            value = mountainArr.get(midd)
            if value == target:
                return midd
            elif value > target:
                low1 = midd +1
            elif value < target:
                high1 = midd -1
        return -1
            