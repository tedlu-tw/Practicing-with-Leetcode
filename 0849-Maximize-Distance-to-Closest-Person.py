class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        st = 0
        m = 1
        for i in range(0, len(seats), 1):
            if seats[i] == 1:
                if st != 0 or (st == 0 and seats[0] != 0):
                    m = max(m, (i - st) // 2)
                elif st == 0 and seats[0] == 0:
                    m = max(m, i - st)   
                st = i
        m = max(m, i - st)    
        return m
