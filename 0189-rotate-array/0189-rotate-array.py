class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(left:int, right:int) -> None:
            swaps = (right - left + 1) // 2
            for i in range(swaps):
                nums[left + i], nums[right - i] = nums[right - i], nums[left + i]

        n = len(nums)
        k %= n

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
