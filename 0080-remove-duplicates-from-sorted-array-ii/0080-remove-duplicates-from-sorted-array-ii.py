class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p_write = 0

        for num in nums:
            if p_write < 2 or num != nums[p_write - 2]:
                nums[p_write] = num
                p_write += 1
        
        return p_write