def boats_counter(nums, limit):
  boats = 0
  left = 0
  nums.sort()
  if nums[-1] > limit: return 'Impossible to save everyone'
  right = len(nums) - 1
  while left <= right:
    if nums[left] + nums[right] <= limit:
      left += 1
    right -= 1
    boats += 1
  return boats

print(boats_counter([3, 2, 2, 1], 3))