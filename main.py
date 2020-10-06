print("(Bartha-Nyiri Adrienn, Subicz Adrián, Szeifert Nóra, Szikszai Ákos)\n")


a = input( "(m) a = " )   #terminálon bekérés a felhasználótól
b = input( "(m) b = " )
c = input( "(m) c = " )
emelet_szam = input("(db) emeletek = ")

a = int(a)   #típus konverzió, mivel az input minden esetben stringet ad
b = int(b)
c = int(c)
emelet_szam = int(emelet_szam)

felszin = emelet_szam*2*c*(a+b)

print(" A szigetelni kívánt felszín: %d m2" % felszin)
