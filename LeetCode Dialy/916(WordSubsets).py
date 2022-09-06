from collections import Counter
from functools import reduce
from itertools import count
from copy import copy
import operator


def fun(words1, words2):
    words = set(words1)
    map = dict()
    for i in words2:
        for j in i:
            count = i.count(j)
            if j not in map or count > map[j]:
                map[j] = count
    for word in words1:
        for j in map:
            if word.count(j) < map[j]:
                words.remove(word)
                break
    return words


words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
words2 = ["lo", "eo"]
print(fun(words1, words2))

# w2 = reduce(operator.or_, map(Counter, words2))
# res = [w1 for w1 in words1 if Counter(w1) >= w2]


def countDict(words2):
    letters = {}
    for i in words2:
        for j in i:
            count = i.count(j)
            if j not in letters or count > letters[j]:
                letters[j] = count
    return letters


# print(countDict(words2))
# print(Counter(words2))
