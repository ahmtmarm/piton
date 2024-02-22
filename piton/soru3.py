#9 a kadar olan sayıların çift sayıların karesi alınarak bir sözlüğe eklenmek istenmektedir.
#keyler orjinal değerler valuelar ise değiştirilmiş değerler olacak.
numbers = range(10)
dict = {}

for n in numbers:
    if n % 2 == 0:
        dict[n] = n ** 2
print(dict)

num = range(10)
dictt = {}
dictt = {n: n ** 2 for n in num if n % 2 == 0}

print(dictt)