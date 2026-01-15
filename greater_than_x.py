numbers = list(map(int, input().split()))
x = int(input())

count = 0
for n in numbers:
    if n > x:
        count += 1

print(count)
