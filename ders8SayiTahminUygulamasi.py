#1-10 arasi rastgele uretilecek sayiyi asagi yukari ifadeleri ile bulun.
#5 hak olsun
#random modulunu kullanin.
#100 uzerinden puanlama yapin ve her soru 20 puan olsun.

import random

sayi=random.randint(1,10)
print(sayi)

denemeHakki=5

while (denemeHakki>0):
    tahmin=int(input('1 ile 10 arasindaki sayiyi tahmin ediniz: '))
    if (tahmin==sayi):
        print(f'tebrikler sayi {sayi} dogru bildiniz')
        break
    else:
        print('sayiyi dogru bilemediniz.')
    denemeHakki-=1
    if denemeHakki==0:
     print('oyun bitii')




