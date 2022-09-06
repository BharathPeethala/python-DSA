# brute force apporach

def can_traverse(start, gas, cost):
    started = False
    i = start
    remaining = 0
    while i != start or not started:
        started = True
        remaining += gas[i]-cost[i]
        if remaining < 0:
            return False
        i = (i+1) % len(gas)
    return True


def bruteForce(gas, cost):
    for i in range(len(gas)):
        if can_traverse(i, gas, cost):
            return i
    return -1


print(bruteForce([1, 5, 3, 3, 5, 3, 1, 3, 4, 5],
      [5, 2, 2, 8, 2, 4, 2, 5, 1, 2]))

gas = [1, 5, 3, 3, 5, 3, 1, 3, 4, 5]
cost = [5, 2, 2, 8, 2, 4, 2, 5, 1, 2]
diff = [gas[i]-cost[i] for i in range(len(gas))]
print(diff)

# Efficeint approach


def efficient_approach(gas, cost):
    n = len(gas)
    remaining = 0
    prev_remaining = 0
    candidate = 0
    for i in range(n):
        remaining += gas[i]-cost[i]
        if remaining < 0:
            prev_remaining += remaining
            remaining = 0
            candidate = i+1
    if prev_remaining+remaining < 0 and candidate == len(gas):
        return -1
    else:
        return candidate


gas = [1, 5, 3, 3, 5, 3, 1, 3, 4, 5]
cost = [5, 2, 2, 8, 2, 4, 2, 5, 1, 2]
print(efficient_approach(gas, cost))
