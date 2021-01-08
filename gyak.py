#!/usr/bin/env python3
from os import read


class Egyszamjatek:
    def __init__(self,tippek,nev):
        self.tippek=tippek
        self.nev=nev
    
    def __str__(self):
        return ' '.join(self.tippek)+" "+self.nev
        
    
def main():
    jatekosok=[]
    with open("egyszamjatek.txt",'r',encoding="iso-8859-1") as f:
        for line in f:
            temp=line.split()
            tippek=[int(szam) for szam in temp[:10]]
            jatekosok.append(Egyszamjatek(tippek,temp[10]))
    print("3.feladat:",len(jatekosok))
    print("4.feladat:",len(jatekosok[0].tippek))
    print("5.feladat")
    tippelt_e=False
    for jatekos in jatekosok:
        if jatekos.tippek[0]==1:
            tippelt_e=True
            break
    if(tippelt_e):
        print("Az első fordulóban valaki tippelt az 1-es számra")
    else:
        print("Az első fordulóban senki sem tippelt az 1-es számra")
    print("6. feladat")
    max_tipp=0
    for jatekos in jatekosok:
        if max(jatekos.tippek)>max_tipp:
            max_tipp=max(jatekos.tippek)
    print(f"A fordulók során a legnagyobb tipp:{max_tipp}")
    beolvasott=int(input("7.feladat: Kérem a forduló sorszámát [1-10]:"))
    if beolvasott>1 and beolvasott>10:
        beolvasott=1
    d=dict()
    for jatekos in jatekosok:
        d[jatekos.tippek[beolvasott-1]]=d.get(jatekos.tippek[beolvasott-1],0)+1
    nyertesszam=100
    for k,v in d.items():
        if v==1:
            if k<nyertesszam:
                nyertesszam=k
    if nyertesszam==100:
        print("8.feladat: Nem volt egyedi tipp a megadott fordulóban!")
    else:
        print(f"8.feladat: A nyertes tipp a megadott fordulóban:{nyertesszam}")
        nyertes_jatekos=""
        for jatekos in jatekosok:
            if jatekos.tippek[beolvasott-1]==nyertesszam:
                nyertes_jatekos=jatekos.nev
        print(f"9.feladat: A megadott forduló nyertese:{nyertes_jatekos}")
        lines=(f"A forduló sorszáma: {beolvasott-1}.\n"
        f"Nyertes tipp: {nyertesszam}\n"
        f"Nyertes játékos: {nyertes_jatekos}\n")
        with open("nyertes.txt",'w',encoding="iso-8859-1") as k:
            k.writelines(lines)
        
    

    
if __name__ == "__main__":
    main()
