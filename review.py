data = []
x = 0
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		x += 1
		if x % 10000 == 0:
			print(len(data))
print(len(data))
print(data[10])
s = 0
for d in data:
	s += len(d)
print(s/len(data))
new = []
for n in data:
	if len(n) < 100:
		new.append(n)
print(len(new))