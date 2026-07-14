class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p_write = 0
        prev = None

        for num in nums:
            if prev is not None and num == prev:
                counter += 1
            else:
                counter = 1
            
            if counter <= 2:
                nums[p_write] = num
                p_write += 1
            
            prev = num
        
        return p_write