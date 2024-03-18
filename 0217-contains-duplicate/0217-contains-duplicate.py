class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsMap = {}

        for i in range(len(nums)):
            if nums[i] in numsMap:
                return True
            else:
                numsMap[nums[i]] = 1