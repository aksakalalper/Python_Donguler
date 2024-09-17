## in range()

for indeks in range(2,10):  ##aralıgı belirtilen bir dizi olusturur.
    print(indeks)

for indeks2 in range(50,100,10):
    print(indeks2)

# enumarate ()


mesaj='merhaba dunya'

for harf in enumerate(mesaj): #indeks bilgisine erismek icin kullanilir.
    print(harf)

#zip 

liste1=[1,2,3,4,5]
liste2=['a','b','c','d','e']

print(list(zip(liste1,liste2))) #2 liste indeks bazli eslestrildi.