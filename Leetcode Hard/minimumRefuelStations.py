from heapq import heappop, heappush
from math import inf


def solve(target, startFuel, stations):
    stations.append([target, inf])
    fuel, count, prev = startFuel, 0, 0
    regrets = []
    for pos, gas in stations:
        print(regrets)
        dist, prev = pos - prev, pos
        while regrets and fuel < dist:
            fuel += -heappop(regrets)
            count += 1
        if fuel < dist:
            return -1
        fuel -= dist
        heappush(regrets, -gas)
    return count


print(solve(100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]]))
