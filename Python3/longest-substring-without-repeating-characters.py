"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/1208566494

3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest
substring
without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seenDict = {}
        maxCount = 0
        lastLegalIndex = 0

        for index, letter in enumerate(s):
            if letter in seenDict:
                lastLegalIndex = max(seenDict[letter]+1,lastLegalIndex)
            seenDict[letter] = index
            maxCount = max(maxCount, index - lastLegalIndex+1)
        return maxCount
