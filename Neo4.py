def cikarma(x,y):
    return x-y
def toplama(x,y):
    return x+y
def bolme(x,y):
    return x/y
def carpma(x,y):
    return x*y

while True:
    try:
        a=float(input("İlk sayıyı giriniz: "))
        b=float(input("İkinci sayıyı giriniz: "))
    except ValueError:
        print("Sayı girin!")
        continue
    
    
    while True:
        islem=input("+,-,/,x yapmak istediğiniz işlemin sembolünü giriniz: ")
        if islem=="+":
            print("Sonuç:",toplama(a,b))
            break
        elif islem =="-":
            print("Sonuç:",cikarma(a,b))
            break
        elif islem=="/":
            print("Sonuç:",bolme(a,b))
            break
        elif islem =="x":
            print("Sonuç:",carpma(a,b))
            break
        else:
            print("Lütfen belirtilen sembolleri girin.")
            