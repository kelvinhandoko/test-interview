def palindromeIndex(s):
    if s == s[::-1]:
        return -1
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            if s[left + 1] == s[right] and s[left + 2] == s[right - 1]:
                return left
            return right
        left += 1
        right -= 1
