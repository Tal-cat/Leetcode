'''
Level: easy
Performance: Runtime 23ms, Beats 98.98%, Memory 13.9MB, Beats 6.85%. 
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # START
        # Not easy to handle strings, change to int and deal with number.

        #reverse because it's easy for doing ×10

        s=int("".join(str(i) for i in digits)) + 1
        l=[]
        while s != 0:
            l.append(s % 10)
            s = s // 10
        return reversed(l)
