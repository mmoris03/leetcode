class Solution:
        
    def _build_nums_to_smaller(self, nums: List[int]) -> Dict[int, int]:
        sorted_nums = sorted(nums)
        nums_to_smaller = {}
        for i, num in enumerate(sorted_nums):
            if num not in nums_to_smaller: 
                nums_to_smaller[num] = i
        return nums_to_smaller


    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_to_smaller = self._build_nums_to_smaller(nums)
        return [nums_to_smaller[num] for num in nums]