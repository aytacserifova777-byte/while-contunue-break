balance=500
while True:
    print("1. balansi gosterge")
    print("2. pulu yatir ")
    print("3. pul cixar")
    print("4.cixis")
    secim=input("seciminizi daxil edin:")
    if secim=="1":
        print("balansiniz:",balance)
    elif secim=="2":
        miktar=float(input("yatirilacaq məbləği daxil edin:"))
        if miktar<=0:
            print("yanlis mebleg:")
        else:
            balance+=miktar 
            print("yatirilan mebleg:",miktar,"son balansiniz:",balance)   
    elif secim=="3":
        miktar=float(input("cixardilacaq memlegi daxil edin:"))
        if miktar>balance:
            print("balansiniz kifayet geder vesait yoxdur:")
        else:
            balance-=miktar
            print("cixardacaginiz mebleg:",miktar, "son balansiniz:",balance)
    elif secim=="4":
        print("cixin edildi" , "son balansiniz:", balance)
        break