from copy import copy


def mirror(p, q):
    ext, ref = copy(q), copy(p)
    while(ext & 1 == 0 and ref & 1 == 0):
        ext //= 2
        ref //= 2

    if(ext & 1 == 1 and ref & 1 == 1):
        return 1
    if(ext & 1 == 1 and ref & 1 == 0):
        return 2
    if(ext & 1 == 0 and ref & 1 == 1):
        return 0


print(mirror(3, 1))
