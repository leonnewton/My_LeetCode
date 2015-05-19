class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
      m=n
      s=""
      while(m!=0):
          x=m%26
          m=m/26
          if x!=0:
            s=str(chr(ord('A')+x-1))+s
          else:
            s='Z'+s
            m=m-1
      return s