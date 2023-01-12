class Solution:
  def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
    sol = [0] * n

    for booking in bookings:
      sol[booking[0] - 1] += booking[2]
      if booking[1] < n:
        sol[booking[1]] -= booking[2]

    for i in range(1, n):
      sol[i] += sol[i - 1]

    return sol