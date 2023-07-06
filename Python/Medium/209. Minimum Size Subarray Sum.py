def minSubArrayLen(target: int, nums):
    counts = []
    for i in range(len(nums)):
      count = 1
      add = nums[i]
      for j in range(i + 1, len(nums)):
          if add < target:
              add += nums[j]
              count += 1
          if add >= target:
              counts.append(count)
              break
      else:
        counts.append(count)

    if len(counts) == 0:
        return 0
    return min(counts)
