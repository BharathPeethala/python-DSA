
from collections import defaultdict


def diff(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    return count


def solve(begin, end, wordList):
    map = defaultdict(list)
    for i in range(len(wordList)):
        for j in range(i+1, len(wordList)):
            if diff(wordList[i], wordList[j]) == 1:
                map[wordList[i]].append(wordList[j])
                map[wordList[j]].append(wordList[i])

    for i in range(len(wordList)):
        if diff(begin, wordList[i]) == 1:
            map[begin].append(wordList[i])
            map[wordList[i]].append(begin)
    for i, j in map.items():
        print(i, j)

    queue = list()
    queue.append([begin, 1])
    visited = set()
    visited.add(begin)
    while(len(queue)):
        string = queue[0][0]
        level = queue[0][1]
        print(string, level)
        queue.pop(0)
        nodes = map[string]
        for node in nodes:
            if node not in visited:
                queue.append([node, level+1])
                visited.add(node)
                if node == end:
                    return level+1
    return 0


def solve_eff(begin, end, wordList):
    map = defaultdict(set)
    N = len(wordList)
    word_size = len(begin)
    for i in range(N):
        string = wordList[i]
        for j in range(word_size):
            rex = string[:j]+"*"+string[j+1:]
            map[rex].add(string)
    string = begin
    for j in range(word_size):
        rex = string[:j]+"*"+string[j+1:]
        map[rex].add(string)
    queue = list()
    queue.append([begin, 1])
    visited = set()
    visited.add(begin)
    while(len(queue)):
        string = queue[0][0]
        level = queue[0][1]
        queue.pop(0)
        for j in range(word_size):
            rex = string[:j]+"*"+string[j+1:]
            nodes = map[rex]
            for node in nodes:
                if node not in visited:
                    queue.append([node, level+1])
                    visited.add(node)

                if node == end:
                    return level+1

    return 0


print(solve_eff('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]))
