#Lambda işlevi, küçük bir anonim işlevdir.
#Bir lambda işlevi herhangi bir sayıda bağımsız değişken alabilir,ancak yalnızca bir ifadeye sahip olabilir.
#lambda arguments : expression

#bagımsız degiskene 10 ekleyin ve sonucu döndürün:a

x = lambda a : a + 10
print(x(5))

#bagımsız değiskeni bagımsız degiskenle carpın:a b
x = lambda a, b : a * b
print(x(5, 6))

#Bağımsız değişkeni özetleyin , ve ve iade et sonuç:a b c
x = lambda a, b, c : a + b + c 
print(x(5, 6, 2))

#Lambda'nın gücü, onları anonim olarak kullandığınızda daha iyi gösterilir. başka bir işlevin içindeki işlev.

#her zaman 2 katına çıkan bir işlev yapmak
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))

