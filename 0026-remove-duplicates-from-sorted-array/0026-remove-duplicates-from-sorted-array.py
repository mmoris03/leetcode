class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p_write = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[p_write]:
                continue
            p_write += 1
            nums[p_write] = nums[i]
        return p_write + 1