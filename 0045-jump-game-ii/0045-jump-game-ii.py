class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        min_jumps = 0
        frontier = 0
        farthest = 0
        for curr_pos, jump_length in enumerate(nums[:-1]):
            farthest = max(farthest, curr_pos + jump_length)
            if curr_pos == frontier:
                min_jumps += 1
                frontier = farthest
        return min_jumps