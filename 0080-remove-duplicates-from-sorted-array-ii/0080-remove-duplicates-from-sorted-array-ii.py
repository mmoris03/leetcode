class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p_write = 0
        seen = {}
        
        for num in nums:
            seen[num] = seen[num] + 1 if num in seen else 1
            if seen[num] <= 2:
                nums[p_write] = num
                p_write += 1
        
        return p_write