class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        brack = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            print(char)
            if char in brack.values():
                stack.append(char)
            else: 
                if not stack or stack[-1] != brack[char]:
                    return False 
                stack.pop()

        if len(stack) == 0:
            return True
        else:
            return False

            
        