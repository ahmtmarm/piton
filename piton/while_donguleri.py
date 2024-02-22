#while döngüsü ile, bir koşul doğru olduğu sürece bir dizi ifadeyi çalıştırabiliriz.
#i 10'dan küçük olduğu sürece i yazdırın.

i = 1
while i < 10:
    print(i)
    i += 1

#i'yi arttırmazsanız dögü sonsuz kadar devam eder.

#break
#break ifadesi ile döngüyü durdurabiliriz.(koşul doğru iken)
#3 olunca döngüden çıkar.
i = 1
while i < 10:
    print(i)
    if i == 3:
        break
    i += 1

#continue ifadesi geçerli yineleme ve bir sonraki ile devam edin.
# i 3 ise bir sonraki yinelemeye devam edin
i = 0
while i < 10:
  i += 1
  if i == 3:
    continue
  print(i)

#else ifadesi ile bir kod bloğunu bir kez çalıştırabiliriz.
i = 0
while i < 10:
  print(i)
  i += 1
else:
  print("i is no longer less than 10")
