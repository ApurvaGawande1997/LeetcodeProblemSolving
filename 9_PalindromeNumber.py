class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        xcopy=x
        final_num=0
        while(x>0):
            next_num=x%10
            final_num=final_num*10+next_num
            x=x//10
        return final_num==xcopy

