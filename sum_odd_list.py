numbers = list(map(int, input().split()))
sum = 0

for n in numbers:
    if n % 2 != 0:
        sum += n

print(sum)
