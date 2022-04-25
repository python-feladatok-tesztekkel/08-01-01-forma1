class Eredmeny:
    nev=str()
    maxsebesseg=int()

    def __init__(self,nev,maxsebesseg):
        self.nev=nev
        self.maxsebesseg=maxsebesseg

class Verseny:
    eredmenyek=list()

    def __init__(self,adatok:str):
        adat=adatok.split(";")
        for versenyzo in adat:
            adat=versenyzo.split(",")
            ve=Eredmeny(adat[0], int(adat[1]))
            self.eredmenyek.append(ve)

    def  atlag(self)->float:
        osszeg=0
        for eredmeny in self.eredmenyek:
            osszeg=osszeg+eredmeny.maxsebesseg
        atlag= float(osszeg) / len(self.eredmenyek)
        return atlag

    def leggyorsabb(self)->int:
        max=self.eredmenyek[0].maxsebesseg
        for index in range(1,len(self.eredmenyek)):
            if (self.eredmenyek[index].maxsebesseg>max):
                max = self.eredmenyek[index].maxsebesseg
        return max

    def leglassabb(self)->int:
        min=self.eredmenyek[0].maxsebesseg
        for index in range(1,len(self.eredmenyek)):
            if (self.eredmenyek[index].maxsebesseg<min):
                min = self.eredmenyek[index].maxsebesseg
        return min
rn 0




