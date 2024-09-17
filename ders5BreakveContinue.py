isim='ahmet yilmaz'

for harf in isim:
    if harf=='t': # 't' harfine geldiğinde donguyu kirar.
        break
    print(harf)

isim2='mehmet yilmaz'

for harf2 in isim2:
    if harf2=='t': # 't' harfine gelince o döngüyü es geçer ve tekrardan başa döner.
        continue
    print(harf2)
