#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionairy lookup approach
        two_sums = dict()

        for x in range(len(nums)):
            secondPair = target - nums[x]
            if secondPair not in two_sums:
                two_sums[nums[x]] = x
            else:
                return [two_sums[secondPair], x]

        # Brute force approach
        #
        # for idx, x in enumerate(nums):
        #     secondPair = target - x
        #     for idy, y in enumerate(nums):
        #         if secondPair == y:
        #             return [idx,idy]

            
# @lc code=end

