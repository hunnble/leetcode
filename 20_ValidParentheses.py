class Solution:
    def isValid(self, s: 'str') -> 'bool':
        length = len(s)
        if (length == 0):
            return True
        if (length < 2 or length % 2 == 1):
            return False
        signal = 0
        parenthesis = []
        for i in range(len(s)):
            length = len(parenthesis)
            char = s[i]
            if char == '(':
                signal += 1
                parenthesis.append(char)
            elif char == ')' and length > 0 and parenthesis[length - 1] == '(':
                signal -= 1
                parenthesis.pop()
            elif char == '{':
                signal += 10
                parenthesis.append(char)
            elif char == '}' and length > 0 and parenthesis[length - 1] == '{':
                signal -= 10
                parenthesis.pop()
            elif char == '[':
                signal += 100
                parenthesis.append(char)
            elif char == ']' and length > 0 and parenthesis[length - 1] == '[':
                signal -= 100
                parenthesis.pop()
        return signal == 0
