class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        products_lr = [0] * n
        products_rl = [0] * n
        acc_lr = 1
        acc_rl = 1
        for i in range(n):
            products_lr[i] = acc_lr
            acc_lr *= nums[i]
            
            rev_idx = n - 1 - i
            products_rl[rev_idx] = acc_rl
            acc_rl *= nums[rev_idx]

        return [
            products_lr[i] * products_rl[i]
            for i in range(n)
        ]