import random

N = float(input("Please enter the number of times"))
i = 0
n = 0
while N > i:
    i += 1
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x * x + y * y < 1:
        n += 1
pi = 4 * n / N
print(f"pi = {pi}")
