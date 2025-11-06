class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        negative=0
        temp=x
        sumnum=0
        if x<0:
            negative=1
            temp=temp*(-1)

        while(temp>0):
            num=temp%10
            if sumnum > (INT_MAX - num) // 10:
                return 0
            sumnum=sumnum*10+num
            temp=temp//10

        if negative==1:
            sumnum=sumnum*(-1)

        

        return sumnum
