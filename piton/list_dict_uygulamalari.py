#Uygulama 1
#Bir Veri Setindeki Değişken İsimlerini Değiştirmek

def dataset(string):
    for i in range(len(string)):
        string[i] = string[i].upper()
    print(string)
data = ['total','speeding','alcohol','not_distracted']
dataset(data)

#LIST COMPREHENSİONS ile değiştirmek
data = ['total','speeding','alcohol','not_distracted']
# Her bir öğeyi büyük harflerle değiştirelim ve yeni listeyi oluşturalım
new_data = [item.upper() for item in data]
print(new_data)

#Uygulama2
eski_fiyat = {'süt': 1.02, 'kahve': 2.5, 'ekmek': 2.5} #bu satır dict oluşturur ve eski fiyatları içerir.
dolar_tl = 0.76 #bu satır bir değişken tanımlar.
yeni_fiyat = {item: value*dolar_tl for (item, value) in eski_fiyat.items()}#bu satır dict comprehension kullanılarak yeni bir sözlük oluşturur.dolar_tl ile çarpılarak yeni fiyatlar oluşur.
print(yeni_fiyat)

#Uygulama3
original_dict = {'ahmet': 38, 'mehmet': 48, 'ali': 57, 'veli': 33}#bu satır dict olusturur ,isimler ve yaşları vardır.
dict2 = {k: v for (k, v) in original_dict.items() if v % 2 == 0}#bu satır original_dict sözlüğündeki yaşların çift olanlarını dict2'ye ekler.
print(dict2)
