data = []
x = 0
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		# x += 1
		# if x % 10000 == 0:
		# 	print(len(data))
wc={}
for a in data:
	lines = a.split()
	for b in lines:
		if b in wc:
			wc[b] += 1
		else:
			wc[b] = 1
for c in wc:
	if wc[c] > 100000:
		print(c, wc[c])

while True:
	word = input('請輸入查詢字詞:')
	if word == 'q':
		print('thanks')
		break
	elif word in wc:
		print(wc[word])
	else:
		print('查無資料')




# print(len(data))
# print(data[10])
# s = 0
# for d in data:
# 	s += len(d)
# print(s/len(data))
# new = []
# for n in data:
# 	if len(n) < 100:
# 		new.append(n)
# print(len(new))
# good = []
# for g in data:
# 	if 'good' in g:
# 		good.append(g)
# print(len(good))