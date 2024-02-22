#Soru

#Aşağıdaki şekilde string değiştiren fonksiyon yaz.

#before: "hi my name is john and i am learning python
#after: "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"

def func(string):
    result = ""
    for i in range(len(string)):
        if i % 2 == 0:
            result += string[i].upper()
        else:
            result += string[i].lower()
    print(result)
func("merhaba benim adım Ahmet ve ben python öğreniyorum")

data = ['total','speeding','alcohol','not_distracted']

# Her bir öğeyi büyük harflerle değiştirelim ve yeni listeyi oluşturalım
new_data = [item.upper() for item in data]

print(new_data)


