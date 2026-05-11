class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        s_sorted = sorted(s)
        t_sorted = sorted(t)

        if t_sorted == s_sorted:
            return True
        return False
