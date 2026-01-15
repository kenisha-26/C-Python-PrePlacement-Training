numbers = list(map(int, input().split()))
count = 0

for n in numbers:
    if n % 2 != 0:
        count += 1

print(count)
