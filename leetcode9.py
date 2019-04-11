class Solution:
    def isPalindrome(self, x):
        #字符串解法
        # x= str(x)
        # print(x)
        # y = list(x)
        # y.reverse()
        # y = ''.join(y)
        # print(type(y))
        # print(y)
        # if x==(y):
        #     return True
        # else:
        #     return False
        #重建回文解法
        if x < 0: return False
        temp = []
        z = x + 0
        while x:
            temp.append(x%10)
            x = x//10
        y = 0
        for i in range(len(temp)):
            j = len(temp) - 1 - i
            y += temp[i] * pow(10,j)
        if z == y:return True
        else: return False
