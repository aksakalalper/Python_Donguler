sayilar=[1,3,5,7,9,12,19,21]

#1 listedeki hangi sayilar ucun katidir?
for indeks1 in sayilar:
 if(indeks1%3==0):
  print(f'dizinin {indeks1} indeksi 3 un katidir.')
 else:
  print(f'dizinin {indeks1} indeksi 3 un kati degildir.')

#2 istedeki sayilarin toplami nedir?
toplamSonuc=0
for indeks2 in sayilar:
 toplamSonuc=toplamSonuc+indeks2
print(toplamSonuc)

#3 listedeki tek sayilarin karesini aliniz.
for indeks3 in sayilar:
 if(indeks3%2==0):
  print(f'dizinin indeksi {indeks3} cift sayidir karesi alinmaz.')
 else:
  kare=indeks3**2
  print(f'dizinin indeksi {indeks3} tek sayidir karesi.{kare}')

sehirler=['kocaeli','istanbul','ankara','izmir','rize']

#4 sehirlerin hangileri en fazla 5 karakterlidir.
for indeks4 in sehirler:
  intIndeks4=int(sehirler.index(indeks4))
  a=int(len(indeks4))
  if (a<6 and a!=5):
   print(f'dizinin {intIndeks4} indeksi uzunlugu {a} olup 5 ten kucuktur.')
  elif (a==5):
   print(f'dizinin {intIndeks4} indeksi uzunlugu {a} olup 5 e esittir.')
  else:
   print(f'dizinin {intIndeks4} indeksi uzunlugu {a} olup 5 ten buyuktur.')

urunler=[
 {'isim':'s6','fiyat':'3000'},
 {'isim':'s7','fiyat':'4000'},
 {'isim':'s8','fiyat':'5000'},
 {'isim':'s9','fiyat':'6000'},
 {'isim':'s10','fiyat':'7000'}
]

#urunlerin toplam fiyatı nedir?
toplamSonuc2=0
for indeks5 in urunler:
 fiyat=int(indeks5['fiyat'])
 toplamSonuc2+=fiyat
 print(toplamSonuc2)

   