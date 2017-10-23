def answer(data, n):
	dic = {}
	ans = []
	
	for x in data:
		if x in dic:
			dic[x] += 1
		else:
			dic[x] = 1
	
	for x in data:
		if dic[x] <= n:
			ans.append(x)

	return ans