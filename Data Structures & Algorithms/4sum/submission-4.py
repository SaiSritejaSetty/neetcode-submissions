class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for x in range(len(nums)):
            if x > 0 and nums[x] == nums[x-1]:
                    continue
            for y in range(x+1, len(nums)):
                if y>x+1 and nums[y] == nums[y-1]:
                    continue
                l = y+1
                r = len(nums)-1
                while l<r:
                    sums = nums[x] + nums[y] + nums[l] + nums[r]
                    if sums < target:
                        l+=1
                    elif sums > target:
                        r-=1
                    else:
                        res.append([nums[x],nums[y],nums[l],nums[r]])
                        l+=1
                        r-=1
                        while l<r and nums[l] == nums[l-1]:
                            l+=1
                        
        return res

                
        