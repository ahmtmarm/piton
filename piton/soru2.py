#ögrencileri oluşturun
#öğrenciler fonksiyonu oluşturun
#çift indexte yer alan ögrencileri bir listeye alınız.
#tek indexte yer alan ögrencileri başka bir listeye alınır
#fakat bu iki liste tek bir liste olarak return olsun.

ogrenciler = ["Ahmet" , "Kaan", "Aysem", "Deniz", "Aybüke", "Kaan"]

def func(ogrenciler):
    groups = [[], []]
    for index, i in enumerate(ogrenciler):
        if index % 2 == 0:
            groups[0].append(i)
        else:
            groups[1].append(i)
    print(groups)
    return groups
func(ogrenciler)