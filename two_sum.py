# if array is not sorted
# space complexity: O(n)
# time complexity: O(n)

def two_sum(nums, target):
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return []


print(two_sum([3, 4, 6, 10], 9))


# if array is sorted
# space complexity: O(1)
# time complexity: O(n)
def two_sum_sorted(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        if current_sum < target:
            left += 1
        else:
            right -= 1
    return []
