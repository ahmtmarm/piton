#KOŞULLAR IF..ELSE
#Python,mantıksal koşulları destekler

#if
a = 35
b = 20
if a > b:
    print("a is greater than b")

#elif
#Python önceki koşullar doğru değilse bu koşula bakar.
a = 35
b = 20
if b > a:
    print("b is greater than a")
elif a > b:
    print("a is greater than b") 

#else
#önceki koşullar doğru değilse herşeyi yakalar.
a = 35
b = 20
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal") 
else:
    print("a is greater than b")

#Tek satır if else deyimi
x = 3
y = 10
print("x") if x > y else print("Y")

#AND
x = 3
y = 10
k = 300
if x < y and k > y:
    print("Both conditions are True")

#OR
x = 3
y = 10 
k = 300
if x < y or y > k:
    print("At least one of the conditions is True")

#NOT
x = 3
y = 10
if not x > y:
    print("x is not greater than y")

#İç içe if
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#PASS   
a = 35
b = 20
if b == a:
    pass
elif a > b:
    print("a is greater than b") 
