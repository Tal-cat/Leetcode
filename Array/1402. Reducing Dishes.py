class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        if satisfaction == []:
            return 0
        # sort in decrease order
        satisfaction.sort(reverse = True)

        if satisfaction[0] <= 0:
            return 0
            
        # 这里化乘法为加法！！！
        presum = 0
        total = 0
        for i in satisfaction:
            # Key idea
            presum += i
            if presum < 0:
                break
            else:
                total += presum
        
        return total
