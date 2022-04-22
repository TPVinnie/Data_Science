a = 10
b = 20
c = a + b
print(c)
a += c
print(a + b)
print(c*a)

str = "great"

i = 0
j = 0
while i < 10:
    while j < 10:
        print(i, j)
        j += 1
    i += 1


lst = (1, 3, 8, 9, 6, 8, 7)
for item in lst:
    print(item)
