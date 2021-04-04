d = {"a":500, 'b':5874, "c":560, "d":400, "e":5874, "f":20}
inverse = [(value, key) for key, value in d.items()]
print max(inverse)[1]
print max(inverse)[2]
print max(inverse)[3]