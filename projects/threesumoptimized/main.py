class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # brute force is fix one number and then apply two-sum - complexity will be (O(n^2))
        # smarter approach: sort the array, from left to right, fix one number - if it is greater than 0, then skip simply and return. if number is duplicate of the previous number, then skip. finally fix that number, then move left (i+1) and right (n-1) pointers inwards until sum is 0. if any of left or right has duplicates, then skip to remove duplicates.
        nums.sort()
        print(nums)
        n = len(nums)
        results = []
        for i in range(n-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = n-1
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if three_sum == 0:
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    results.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
        return results