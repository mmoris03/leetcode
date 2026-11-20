class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n

        prefix_prods = 1
        for i in range(n):
            res[i] = prefix_prods
            prefix_prods *= nums[i]

        suffix_prods = 1
        for i in reversed(range(n)):
            res[i] *= suffix_prods
            suffix_prods *= nums[i]

        return res