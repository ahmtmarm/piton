#For Döngüleri
#bir dizi üzerinde yineleme yapmak için kullanılır.
myfam = ["Ahmet","Ali","Ümmü","Deniz"]
for x in myfam:
    print(x)

#MARIM kelimesindeki harfler arasında dolaşın.
for a in "MARIM":
    print(a)

#break ifadesi ile durdurabiliriz
myfam = ["Ahmet","Ali","Ümmü","Deniz"]
for x in myfam:
    if x == "Ümmü":
        break
    print(x)

#continue ifadesi ile atlayabiliriz
myfam = ["Ahmet","Ali","Ümmü","Deniz"]
for x in myfam:
    if x == "Ahmet":
        continue
    print(x)

#Range fonksiyonu ile 10'a kadar olan rakamları yazar( 0 to 9)
for x in range(10):
    print(x)

#2 to 5
for x in range(2, 6):
  print(x)

#2 den baslar 3'er 3'er artar
for x in range(2, 30, 3):
  print(x)

#if else in for loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#Nestel loops
#iç içe geçmiş bir döngü
#iç döngü ve dış döngü her yinelemesi için bir kez çalışcaktır.
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)

