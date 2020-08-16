def strStr(self, haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if len(needle) > len(haystack):
        return -1
    if len(needle) == len(haystack):
        return 0 if needle == haystack else -1

    j = len(needle)
    for i in range(len(haystack)-j+1):
        if haystack[i:i+j] == needle:
            return i

    return -1
