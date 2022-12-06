import string

#szöveg

szoveg ="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

#1 feladat

print(len(szoveg))

#2 feladat

print("Ennyi írásjel van a szövegben: ",szoveg.count('.'))

#3 feladat

lorem = szoveg.replace("Lorem","LOREM")
print(lorem)  
  
#4 feladat

szamok = []
betu = []

for b in szoveg:
    if (b.isalpha()):
        betu.append(b)
    elif (b.isalnum()):
        szamok.append(int(b))    

print("számok",szamok)
print("szövegben ennyi karakter van: ",len(szoveg),"szóközel")
print("szövegben ennyi karakter van: ",len(betu),"szóköz nélkül")

#5 feladat

kszo = str(input("Adja meg a kesett szót: "))
if kszo in  szoveg:
    print("Megvan a szó:",kszo,"a szövegben")
    print("Ennyiszer találta meg a szót",kszo.count(kszo),"szer/szor")
else:
    print("Nincsen ilyen szó a szövegben")   
    print("Ennyiszer találta meg a szót",kszo.count(kszo),"szer/szor")
    

