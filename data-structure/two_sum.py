def two_sum_sorted(nums, target):
    pos1 = 0
    pos2 = len(nums) - 1
    while pos1 < pos2:   
        if nums[pos1] + nums[pos2] == target:
            return [pos1, pos2]
        elif nums[pos1] + nums[pos2] < target:
            pos1 += 1
        elif nums[pos1] + nums[pos2] > target:
            pos2 -= 1
        
#test
print(two_sum_sorted([1, 2, 3, 4, 6], 6))