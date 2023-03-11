n = int(input())
lst = []
for i in range(n):
    tup = tuple(map(int, input().split()))
    lst.append(tup)
lst.sort(key=lambda x: (x[0], -x[1], x[2]))
for tup in lst:
    ntup = ",".join(str(x) for x in tup)
    print(ntup)
