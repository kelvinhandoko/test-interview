def anagram(s):
    if len(s) % 2 != 0:
        return -1

    half = len(s) // 2
    s1 = s[:half]
    s2 = s[half:]

    freq1 = [0] * 26
    freq2 = [0] * 26

    for ch in s1:
        freq1[ord(ch) - ord('a')] += 1

    for ch in s2:
        freq2[ord(ch) - ord('a')] += 1

    changes = 0
    for i in range(26):
        if freq1[i] > freq2[i]:
            changes += freq1[i] - freq2[i]

    return changes
