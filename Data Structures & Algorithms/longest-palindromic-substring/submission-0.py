class Solution:
    def longestPalindrome(self, s: str) -> str:
        #return the longest substring
        longest = s[0:1]

        #some sort of grid that says between i and j, this is or is not a palindrome

        isPalindrome = [[False]* (len(s)) for _ in range(len(s))]

        #start with the base case 
        # b is palindrome, a is palindrome
        for i in range(0, len(s)):
            isPalindrome[i][i] = True

        #build it up
        # b a not a palindrome ... ab not a palindrome
        for i in range(0, len(s)-1):
            j = i + 1
            if s[i] == s[j]:
                isPalindrome[i][j] = True
                if len(longest) < 2:
                    longest = s[i:j+1]

        # keep building it
        # diff can go from 2 to len(s) - 1
        # if diff is 2, then i can be 5 - 2 - 1
        for length in range (2, len(s)):
            for i in range (0, len(s) - length):
                j = i + length
                if s[i] == s[j] and isPalindrome[i+1][j-1]:
                    isPalindrome[i][j] = True
                    if len(s[i:j+1]) > len(longest):
                        longest = s[i:j+1]

        return longest;             
        

        