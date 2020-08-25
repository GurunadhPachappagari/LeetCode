class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        bucket = {}
        i = 0
        j = -1
        length = 0
        maxLen = 0
        while i< len(s):
            # print(s[i],end=" ")
            if s[i] not in bucket.keys():
                length += 1
                maxLen = max(length,maxLen)
                bucket[s[i]] = i
                i += 1
            else:
                for k in range(j+1,bucket[s[i]]):
                    bucket.pop(s[k])
                j = bucket[s[i]]
                bucket[s[i]] = i
                length = i-j
                i += 1
            # print(maxLen)
        return maxLen