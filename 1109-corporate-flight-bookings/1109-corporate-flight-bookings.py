class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0] * (n+1)
        for booking in bookings:
            ans[booking[0]-1] += booking[2]
            ans[booking[1]] -= booking[2]
        
        tmp = 0
        for i in range(n):
            tmp += ans[i]
            ans[i] = tmp
        
        return ans[:n]


