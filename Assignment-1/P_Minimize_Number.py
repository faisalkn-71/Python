def max_operations(n, a):
    operations = 0
    while all(x % 2 == 0 for x in a):
        a = [x // 2 for x in a]
        operations += 1
    return operations

n = int(input())
a = list(map(int, input().split()))

print(max_operations(n, a))
