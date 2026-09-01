class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashnum = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashnum:
                return [hashnum[diff], i]
            hashnum[n] = i