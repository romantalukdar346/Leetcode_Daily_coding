def minTimeToVisitAllPoints(self, points):

    count=0

    for i in range(1,len(points)):

        count+=max(abs(points[i-1][0]-points[i][0]),abs(points[i-1][1]-points[i][1]))

    return count