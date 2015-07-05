class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        len1 = len(nums)
        i = 0
        sum = 0
        max = 0
        max_b = nums[0]
        while i < len1:
            if nums[i] > 0:
                sum = nums[i]
                if sum > max:
                    max = sum
                i = i + 1
                while i < len1 and sum + nums[i] > 0:
                    sum = sum + nums[i]
                    if sum > max:
                        max = sum
                    i = i + 1

            else:

                if nums[i] > max_b:
                    max_b = nums[i]
                i = i + 1
        if max > 0:
            return max
        else:
            return  max_b










if __name__ == '__main__':
    nums = [-5,-2,-3,0]
    s = Solution()
    print s.maxSubArray(nums)




