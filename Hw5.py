even = []
odd = []

for n in range(1, 51, 1):
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

print("Even Numbers:", even)
print("Odd Numbers:", odd)
