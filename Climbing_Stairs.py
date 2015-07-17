class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
       result = [0]*(n + 1)
       if n == 1:
           return 1
       if n == 2:
           return 2
       result[1] = 1
       result[2] = 2
       for i in range(3,n+1):
           result[i] = result[i-1] + result[i-2]

       print result
       print result[n]
       return result[n]



if __name__ == '__main__':
    s = Solution()
    print s.climbStairs(1)