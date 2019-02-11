class Solution:
    def countAndSay(self, n: 'int') -> 'str':
        res = '1'
        tmp = res
        for _ in range(n - 1):
            count = 1
            i = 0
            tmp = ''
            while i < len(res) - 1:
                if  res[i] == res[i + 1]:
                    count += 1
                else:
                    tmp += str(count) + res[i]
                    count = 1
                i += 1
            tmp += str(count) + res[i]
            res = tmp
        return res
