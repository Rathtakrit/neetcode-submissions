class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      seen = {}
      for i, vals in enumerate(nums):
        check = target - vals
        if check in seen:
            return [seen[check],i]
        else :
            seen[vals] = i