class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n <= 2:
            return n
        
        p_write = 2
        for i in range(2, n):
            if nums[i] != nums[p_write - 2]:
                nums[p_write] = nums[i]
                p_write += 1
        
        return p_write