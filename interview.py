'''

Problem Statement #

Given an array of positive numbers and a positive number ‘k,’
find the maximum sum of any contiguous subarray of size ‘k’.
Example 1:
Input: [2, 1, 5, 1, 3, 2], k=3
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
Example 2:
Input: [2, 3, 4, 1, 5], k=2
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
'''


def max_sum_subarray(arr, k):
    result = 0
    length = len(arr)
    for i in range(length):
        if i+k>length:
            break
        sub_arr = arr[i:i+k]    # 0 :  0+3 = 2
        sum_value = sum(sub_arr)
        if sum_value > result:
            result = sum_value
    return result


input_arr = [2, 1, 5, 1, 3, 2]
print(max_sum_subarray(input_arr, 3))
input_arr = [2, 3, 4, 1, 5]
print(max_sum_subarray(input_arr, 2))

