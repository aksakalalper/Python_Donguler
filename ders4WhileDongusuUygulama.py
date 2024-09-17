
'''
sayilar=[1,3,5,7,9,12,19,21]

#1 listeyi while dongusu ile ekrana yazdirin.
indeks=0
listeUzunlugu=len(sayilar)
while (indeks<=(listeUzunlugu-1)):
    print(sayilar[indeks])
    indeks+=1

#2 baslangic ve bitis degerlerini kullanicidan alip aradaki tum tek sayilari ekrana yazdirin.
baslangicDegeri=int(input('dizi baslangic degerini giriniz:'))
bitisDegeri=int(input('bitis degerini giriniz: '))
while (baslangicDegeri<=bitisDegeri):
    if(baslangicDegeri%2==0):
        print(baslangicDegeri)
    baslangicDegeri+=1

#3 1-100 arasindaki sayilari azalan sekilde yazdirin.
iindeks2=100
while (1<=iindeks2):
    print(iindeks2)
    iindeks2-=1

    
#4 kullanicidan alinan 5 sayiyi ekranda sirali sekilde yazdirin.
sayilar2=[]
indeks3=0
while (indeks3<=4):
  sayilar2.append(int(input(f'{indeks3}indeksindeki sayiyi giriniz')))
  indeks3+=1
  sayilar2.sort()
print(sayilar2)  
'''

#5 kullanicidan sinirsiz urun bilgisini alip urun listesine ekleyin (fiyat-urun)
# urun sayisini kullaniciya sorun
# sozluk yapisini kullanin
urunler=[]
adet=int(input('kac adet urun girilecek: '))
i=0

while(i<adet):
  isim=input('urun ismi giriniz: ')
  fiyat=input('fiyat giriniz: ')
  urunler.append({
    'isim':isim, 
    'fiyat':fiyat
  })
  i+=1  

for urun in urunler:
  print(urunler)

