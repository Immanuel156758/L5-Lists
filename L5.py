marks=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
high=[]
average=[]
low=[]

for c in marks:
	if c > 70:
		high.append(c)
	elif c < 40:
		low.append(c)
	else:
		average.append(c)
	
print(high)
print(average)
print(low)