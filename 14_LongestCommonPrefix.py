class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        if not strs:
            return ''
        for i, letters in enumerate(zip(*strs)):
            if len(set(letters)) > 1:
                return strs[0][:i]
        return min(strs, key=len)