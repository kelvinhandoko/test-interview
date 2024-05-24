# Description: Given a string, find the length of the longest substring without repeating characters.
# Example:
# Input: "abcabcbb"
# Output: 3

# space complexity: O(1)
# time complexity: O(n^2)
def longSubStringWithoutRepeating(word):
    n = len(word)
    res = 0
    for i in range(n):
        visited = [0] * 256
        for j in range(i, n):
            if visited[ord(word[j])]:
                break
            else:
                res = max(res, j - i + 1)
                visited[ord(word[j])] = True
        visited[ord(word[i])] = False
    return res


print(longSubStringWithoutRepeating("abcabcbb"))  # 3
