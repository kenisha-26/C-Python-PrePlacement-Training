# Program to check divisibility by 5 and 11

n = int(input())

if n % 5 == 0 and n % 11 == 0:
    print("Divisible")
else:
    print("Not Divisible")
