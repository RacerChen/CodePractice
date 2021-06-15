""""
    @Category: Max Sub Array
    @Date: 2021/06/10 21:59PM
"""
from typing import List


# Merge Algorithms
def max_cross_mid(nums: List[int], low, mid, high) -> int:
    if high - low == 1:
        return nums[low]
    left_sum = nums[mid]
    total_sum = nums[mid]
    for i in range(mid, low - 1, -1):
        total_sum += nums[i]
        if total_sum > left_sum:
            left_sum = total_sum
    right_sum = nums[mid + 1]
    total_sum = nums[mid + 1]
    for j in range(mid + 1, high):
        total_sum += nums[j]
        if total_sum > right_sum:
            right_sum = total_sum
    return left_sum + right_sum - nums[mid] - nums[mid + 1]


def max_in_sub_array(nums: List[int], low, high) -> int:
    if high == low or high - low == 1:
        return nums[low]
    else:
        mid = int((low + high) / 2)
        left_sum = max_in_sub_array(nums, low, mid)
        right_sum = max_in_sub_array(nums, mid + 1, high)
        cross_sum = max_cross_mid(nums, low, mid, high)
        if left_sum >= cross_sum and left_sum >= right_sum:
            return left_sum
        elif right_sum >= cross_sum and right_sum >= left_sum:
            return right_sum
        else:
            return cross_sum


def maxSubArray_merge(nums: List[int]) -> int:
    return max_in_sub_array(nums, 0, len(nums) - 1)


# Dynamic Programming
def maxSubArray_dp(nums: List[int]) -> int:
    dp = [nums[0]]
    max_sub_arr = dp[0]
    for i in range(1, len(nums)):
        dp.append(max(dp[i - 1] + nums[i], nums[i]))
        max_sub_arr = max(max_sub_arr, dp[i])
    return max_sub_arr


if __name__ == '__main__':
    nums_list = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    _low = 0
    _high = len(nums_list)
    _mid = int((_low + _high) / 2)
    print(max_cross_mid(nums_list, _low, _mid, _high))

    print(maxSubArray_merge(nums_list))

    # print(maxSubArray_dp(nums_list))
