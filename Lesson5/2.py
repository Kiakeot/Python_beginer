d = {"a":500, 'b':5874, "c":560, "d":400, "e":5874, "f":20}
print(d)
max1 = max(d.values())
for y in range(3):
	for i in d.items():
		if i[1] == max(d.values()):
	 		d.pop(i[0])
	 		break
print(d)