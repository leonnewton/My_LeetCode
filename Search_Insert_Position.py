class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}

    def binary_search(self,nums,low,high,number):
        while low <= high:
            mid = (low + high) / 2
            if nums[mid] == number:
                return mid
            elif nums[mid] < number:
                low = mid + 1
            else:
                high = mid - 1
        return low



if __name__ == '__main__':
    nums = [1]
    a = Solution()
    result = a.binary_search(nums,0,len(nums)-1,2)
    print result
