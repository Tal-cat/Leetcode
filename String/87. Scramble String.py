class Solution:
    @lru_cache(maxsize = None) # will cause TLE without it
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if Counter(s1) != Counter(s2):
            return False
        L = len(s1)
        for k in range(1, L):
            # 检验前后交换的情况
            if self.isScramble(s1[0:k], s2[0:k]) and self.isScramble(s1[k:], s2[k:]):
                return True
            if self.isScramble(s1[0:k], s2[L-k:]) and self.isScramble(s1[k:], s2[0:L-k]):
                return True
        
        return False
