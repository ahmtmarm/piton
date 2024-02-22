#Classes&Objects
#Python,nesne yönelimli bir programlama dilidir.

#Class

class myClass:
    x = 5
p1 = myClass()
print(p1.x)

# __init__() işlevi
#Tüm sınıfların __init__() adında bir işlevi vardır.
#Nesne özelliklerine veya diğer nesnelere değer atamak için __init__() işlevini kullanın.
#Müşteri adında bir sınıf oluşturalım ve değer atamak için __init__() işlevini kullanalım.

class musteri:
    def __init__(self,name,age,):
        self.name = name
        self.age = age
mus1 = musteri("Alexa", 45)
print(mus1.name)
print(mus1.age)

#__init__() fonksiyonu otomatik olarak çağrılan bir fonksiyondur.

#__str__()fonksiyonu
#Bu metod,bir nesneyi "dizgesel olarak temsil etmek" için kullanılır.
#Yani,bir nesnenin insanlar tarafından okunabilir bir biçimde dize temsilini döndürmek için kullanılır.

class musteri:
    def __init__(self,name,age,):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}({self.age})"
mus1 = musteri("Alexa", 45)
print(mus1)

#Object Methods

class musteri:
    def __init__(self,name,age,):
        self.name = name
        self.age = age
    
    def myfunc(self):
        print("Your client's name is "+ self.name +" and he is " + str(self.age) + " years old")
mus1 = musteri("Alexa", 45)
mus1.myfunc()

#nesnelerdeki özellikleri degistirebilirsiniz mus1.age = 40 gibi
#del mus1.age mus1 nesnesinde age özelliğini siler
#del mus1 mus1 nesnesini siler
#class tanımları boş olamaz ama içeriği olmayan bir tanımınız varsa pass kullanabilirsiniz.
#class musteri:
    #pass

