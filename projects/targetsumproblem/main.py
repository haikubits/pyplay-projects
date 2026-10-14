# https://leetcode.com/problems/target-sum/description/

class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        total_sum = sum(nums)
        if target > total_sum:
            return 0
        # applying the mathematical rule of sets P and N which have positive and negative sign integers, sum(P) = (target + total_sum)/2. All we have to do now is to find all the subsets P which satisfy this condition. Edge cases are if this value (target + total_sum)/2 is odd or negative, then its not possible
        if target + total_sum < 0 or (target + total_sum) % 2 != 0:
            return 0
        s = int((target + total_sum)/2)
        dp = [0] * (s+1)
        dp[0] = 1
        for num in nums:
            for j in range(s, num - 1, -1):
                # two choices, to include or exclude num
                dp[j] += dp[j - num]
        return dp[s]