import heapq
class SeatManager(object):

    def __init__(self, n):
        self.seat_avaliable=list(range(1,n+1))

        

    def reserve(self):
        return heapq.heappop(self.seat_avaliable)
        

    def unreserve(self, seatNumber):
        heapq.heappush(self.seat_avaliable,seatNumber)

        