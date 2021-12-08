def permutations(iterable):
    if len(iterable) == 1:
        yield (iterable[0],)
    else:
        for perm in permutations(iterable[1:]):
            for i in range(len(iterable)):
                yield perm[:i] + (iterable[0],) + perm[i:]


def unique_permutations(iterable):
    return list(set(permutations(iterable)))


def inversions(arr, n):
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if ord(arr[i]) > ord(arr[j]):
                count += 1
    return -1 if count % 2 else 1


permut = sorted([''.join(x) for x in unique_permutations("0123456")])
stepeni = [0] * 7

A = [['x', -1, 6, 4, -1, 6, 8],
     [-9, 5, 3, 9, 5, 'x', -4],
     ['x', -8, 3, -9, 9, 3, -8],
     [1, 8, 9, 'x', -5, -6, 'x'],
     [4, -6, -2, -5, 'x', -7, -2],
     [-5, 1, 'x', -2, -1, 4, 6],
     [-1, 'x', -7, -3, 1, 9, 6]]

for i in range(len(permut)):
    stepen = 0
    mnozhitel = 1
    for j in range(7):
        if A[j][ord(permut[i][j]) - ord('0')] == 'x':
            stepen += 1
        else:
            mnozhitel *= A[j][ord(permut[i][j]) - ord('0')]
    stepeni[stepen] += inversions(permut[i], 7) * mnozhitel
for i in range(7):
    print('x^', i, '   ', stepeni[i], sep='')
