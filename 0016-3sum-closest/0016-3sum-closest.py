class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j < k:
                curSum = nums[i] + nums[j] + nums[k]

                if abs(curSum - target) < abs(closest - target):
                    closest = curSum
                if curSum < target:
                    j+=1
                else:
                    k-=1


        return closest
