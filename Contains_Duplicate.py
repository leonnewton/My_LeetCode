class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
          if len(nums) == 0:
            
            return False

          if len(set(nums)) != len(nums):
           
            return False
          else:
          
            return True