"""generálj 5 véletlen számot 10-35 között"""
import random
def veletlen():
    list=[]   #egy listában azonos típusú adatok legyenek(csak szöveg v csak szám)
    i:int = 0
    while i<5: 
        szam = random.random()*(35-10)+10 # lista végéhez fűzöm az aktuális elemet
        list.append(szam)
        i += 1
    return

listam=veletlen()

"""Írjuk ki egymás alá a lista elemeit"""
def lista_kiir(list):
    for i in range(0,len(list),1):
        print(f"a lista {i} eleme: {list[i]}")

lista_kiir(list)

def lista_kiir2 ():
    n:int = 0
    while n < len(list):
        print(f"a lista {n} eleme: {list[i]}")
        n +1