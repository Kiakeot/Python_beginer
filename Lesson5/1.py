disct = {"apple":1, "orange":2, "banana": 5}
for i in disct.items():
    if i[1] == max(disct.values()):
        print(i[0])
        break