class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        for num in nums:
            if num in seen:
                rep = num
            else:
                seen.add(num)
        for missing in range(1, len(nums) + 1):
            if missing not in seen:
                return [rep, missing]