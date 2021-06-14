# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Example 2:
# Input: nums = [1]
# Output: 1

# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23

# https://leetcode.com/explore/featured/card/top-interview-questions-easy/97/dynamic-programming/566/

# https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/



def maxSubArray(nums):
    max_so_far =nums[0]
    curr_max = nums[0]
    for i in range(1,len(nums)):
        curr_max = max(nums[i], curr_max + nums[i])
        max_so_far = max(max_so_far,curr_max)   
    return max_so_far