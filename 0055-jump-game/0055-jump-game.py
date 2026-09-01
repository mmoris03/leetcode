class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        jump_pos = n - 1
        for i in range(n - 2, -1, -1):
            if i + nums[i] >= jump_pos:
                jump_pos = i
        return jump_pos == 0