from collections import Counter
words = ["a", "b", "c"]
word = 'dede'
pattern = 'a'
pattern_counter = dict(Counter(pattern))


def compare(pattern, word):
    map1 = dict()
    map2 = dict()
    n = len(word)
    i = 0
    while(i < n):
        if word[i] in map1 and map1[word[i]] != pattern[i] or pattern[i] in map2 and map2[pattern[i]] != word[i]:
            return False
        else:
            map1[word[i]] = pattern[i]
            map2[pattern[i]] = word[i]
        i += 1
    return True


def findAndReplace(words, pattern):
    res = list()
    for word in words:
        if len(word) != len(pattern):
            continue
        if compare(pattern, word):
            res.append(word)
    return res


print(findAndReplace(words, pattern))
