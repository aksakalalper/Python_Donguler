#1-100 arasi sayilari yazdirma

x=0

while x<=100: #kosul dogru oldugu surece dongu calisir.
    print(x)
    x+=1

print('dongu bitti.')    

isim='' #false 

while not isim:
    isim=input('isim giriniz')  #isim degiskenine veri girmedikce dongu icinde kalmaya devam eder.
    
print(f'merhaba {isim}')