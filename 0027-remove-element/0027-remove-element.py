class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p_write = 0
        for num in nums:
            if num != val:
                nums[p_write] = num
                p_write += 1
        return p_write