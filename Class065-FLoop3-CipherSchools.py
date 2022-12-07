x = input()
a = ''
for i in range(len(x)):
    if x[i] not in a :
        print(f"{x[i]}: {x.count(x[i])}")
        a = a + x[i]
