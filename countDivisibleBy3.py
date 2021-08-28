# How many numbers less than 904 are divisible by 3?
i = 0
for n in range(1,904):
    if n % 3 == 0:
        i+=1
print(i)
