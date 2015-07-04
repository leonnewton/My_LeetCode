class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        candidate = 0
        count = 0
        for  i in range(len(nums)):
            print 'i',i
            if count == 0:
                candidate = nums[i]
                count = count + 1
            elif candidate == nums[i]:
                     count = count + 1
            else:
                     count = count - 1
        return candidate


if __name__ == '__main__':
    nums = [6,5,5]
    s = Solution()
    print s.majorityElement(nums)