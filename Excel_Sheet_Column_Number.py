class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        len1=len(s)
        m=len1-1
        sum=0
        for j in range(0,len1):
            sum=sum+(ord(s[j])-ord('A')+1)*(26**m)
            m=m-1

        return sum
		
		
		
		
		
		
class Solution:
    # @param {string} s
    # @return {integer}
   def titleToNumber(self, s):
       len1=len(s)
       sum=0
       for i in range(0,len1):
           tmp=ord(s[i])-ord('A')+1
           sum=sum*26+tmp

       return sum