

cipher = input ("enter the cipher text")
freq = []
a= dict()
for char in cipher:
	if char not in freq:
		cnt = cipher.count(char)
		a[char] = cnt
		freq += char 


sorted_items = sorted(a.items(), key=lambda item: item[1], reverse=True)
print(sorted_items)
top = []
first_four = sorted_items[:4]
for key,value in first_four:
	top += key
print (top)

