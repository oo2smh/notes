def twoSum(nums, target):
    # sorted_arr = sorted(nums)
    left = 0
    right = len(nums) - 1
    print("left", left, "right", right)
    while True:
        sum = nums[left] + nums[right]
        print(sum)
        if sum == target:
            return [left, right]
        if sum < target:
            left += 1
        elif sum > target:
            right -= 1

# print(twoSum([3,4,5,6], 7))
print(twoSum([3,2,3], 6))


