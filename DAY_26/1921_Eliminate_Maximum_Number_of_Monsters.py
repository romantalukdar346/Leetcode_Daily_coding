def eliminateMaximum( dist, speed):
    arrival = []
    for i in range(len(dist)):
        arrival.append(dist[i] / speed[i])

    arrival.sort()
    print(arrival)
    ans = 0

    for i in range(len(arrival)):
        if arrival[i] <= i:
            break

        ans += 1

    return ans