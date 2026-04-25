class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            print("The length of both the strings are equal, lets check the characters")
        else:
            return False
        s_sorted = sorted(s)
        t_sorted = sorted(t)

        if s_sorted == t_sorted:
            print("Both strings are Anagram")
            return True
        return False