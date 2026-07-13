class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p_write = 0
        seen = set()
        for num in nums:
            if num in seen:
                continue
            nums[p_write] = num
            seen.add(num)
            p_write += 1
        return p_write