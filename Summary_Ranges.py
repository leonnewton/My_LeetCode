class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        len1 = len(nums)
        i = 0
        result = []
        while i < len1:
            init = nums[i]
            while i + 1 < len1 and nums[i+1] == nums[i] + 1:
                i = i + 1
            if init == nums[i]:
                result.append(str(nums[i]))
            else:
                result.append(str(init) + "->" + str(nums[i]))

            i = i + 1
        return result




if __name__ == '__main__':
    test = [0,1,2,4,5,7]
    s = Solution()
    print s.summaryRanges(test)


