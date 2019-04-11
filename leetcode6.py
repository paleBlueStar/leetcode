class Solution:
    def convert(self, s, n):
        num = len(s);result = []
        if n == 1: return s
        cycle = 2 * n - 2
        for i in range(n):
          j = 0
          while(i + j < num):
            result.append(s[i + j])
            if i != 0 and i != n -1 and j + cycle - i < num:
              result.append(s[j + cycle - i])
            j += cycle
          return ''.join(result)
