class Solution:
  def twoSum(self, nums, target):
      for i in range(len(nums)):
          for j in range(len(nums)):
              if nums[i]+nums[j] == target:
                  return [i,j]

u = Solution()
print(u.twoSum([2,3,5,6,7], 11))