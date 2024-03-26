"""
https://leetcode.com/problems/reverse-only-letters/description/
https://leetcode.com/problems/reverse-only-letters/submissions/1214011163/
917. Reverse Only Letters

Given a string s, reverse the string according to the following rules:

    All the characters that are not English letters remain in the same position.
    All the English letters (lowercase or uppercase) should be reversed.

Return s after reversing it.

 

Example 1:

Input: s = "ab-cd"
Output: "dc-ba"

Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

 

Constraints:

    1 <= s.length <= 100
    s consists of characters with ASCII values in the range [33, 122].
    s does not contain '\"' or '\\'.

"""
class Solution:
    
    def reverseOnlyLetters(self, s: str) -> str:
        alpha = "abcdefghijklmnopqrstuvwxyz"
        alpha =  alpha + alpha.upper()
        list_string = list(s)
        char_stack = []
        for char in list_string:
            if char in alpha:
                char_stack.append(char)
        for index in range(len(list_string)):
            if list_string[index] in alpha:
                list_string[index] = char_stack.pop()
        return ''.join(list_string)
