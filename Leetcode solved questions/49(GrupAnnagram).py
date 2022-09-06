from collections import Counter, defaultdict


def grpAnaram(strs):
    map = defaultdict(list)
    for string in strs:
        count = [0]*26
        for char in string:
            count[ord(char)-ord("a")] += 1
        map[tuple(count)].append(string)

    return map


print(grpAnaram(["ddddddddddg", "dgggggggggg"]
                ))


a = dict(Counter([3, 0, 1, 0]))
a = dict(sorted(a.items(), key=lambda item: item[1], reverse=True))
print(a)
print(list(a.keys()))
