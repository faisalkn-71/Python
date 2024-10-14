from collections import Counter

def min_removals_to_good_sequence(n, a):
    count = Counter(a)
    removals = 0
    
    for x in count:
        if count[x] > x:
            removals += count[x] - x
        elif count[x] < x:
            removals += count[x]
    
    return removals

n = int(input())
a = list(map(int, input().split()))


print(min_removals_to_good_sequence(n, a))
