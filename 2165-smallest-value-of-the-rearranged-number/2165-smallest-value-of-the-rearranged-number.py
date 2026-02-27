class Solution:
    def smallestNumber(self, num: int) -> int:
        nums = sorted(str(abs(num)))

        if num == 0:
            return 0
        
        if num < 0:
            return -int(''.join(nums[::-1]))
        
        i = 0
        while nums[i] == '0':
            i += 1
        
        nums[0], nums[i] = nums[i], nums[0]

        return int(''.join(nums))