from multiprocessing import connection
from sqlite3 import connect
import sqlite3
from winreg import QueryInfoKey
from cats_model import Tevas, Mama, Vaikas, engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from tkinter import *

session = sessionmaker(bind=engine)()
conn = sqlite3.connect('data/cats.db')
c = conn.cursor()

def naudotojo_meniu():
    print("=== Kaciu registras ===")
    print("1 | Prideti nauja katina")
    print("2 | Prideti nauja kate")
    print("3 | Prideti nauja kaciuka")
    print("4 | Katinu sarasas/perziura")
    print("5 | Kaciu sarasas/perziura")
    print("6 | Kaciuku sarasas/perziura")
    #print("7 | Katinu paieska")
    print("8 | Pakeisti irasa")
    print("9 | Panaikinti irasa")
    print("0 | Iseiti")
    pasirinkimas = input("Pasirinkite veiksma: ")
    return pasirinkimas

def prideti_katina():
    katinas = Tevas(
        vardas = input("Vardas: "),
        veislynas = input("Veislynas: "),
        gimimo_data = datetime.strptime(input("Gimimo data (MMMM-MM-DD): "), "%Y-%m-%d"),
        kilmes_salis = input("Kilmes salis: "),
        lytis = input("Lytis: ")
    )
    session.add(katinas)
    session.commit()
    print(katinas)
    return katinas

def prideti_kate():
    kate = Mama(
        vardas = input("Vardas: "),
        veislynas = input("Veislynas: "),
        gimimo_data = datetime.strptime(input("Gimimo data (MMMM-MM-DD): "), "%Y-%m-%d"),
        kilmes_salis = input("Kilmes salis: "),
        lytis = input("Lytis: ")
    )
    session.add(kate)
    session.commit()
    print(kate)
    return kate
    
def prideti_kaciuka():
    gimes_kaciukas = Vaikas(
        vardas = input("Vardas: "),
        veislynas = input("Veislynas: "),
        gimimo_data = datetime.strptime(input("Gimimo data (MMMM-MM-DD): "), "%Y-%m-%d"),
        kilmes_salis = input("Kilmes salis: "),
        isvyko_gyventi = input("Isvyko gyventi: "),
        lytis = input("Lytis: "),
        #katinas_id = katinas_id,
        #kate_id = kate_id
)
    katinai = session.query(Tevas).all()
    for katinas in katinai:
        print(katinas.id, katinas.vardas, katinas.veislynas, katinas.gimimo_data, katinas.kilmes_salis, katinas.lytis)
    katinai = input("Pasirinkite katino ID: ")
    katinas.vaikai.append(gimes_kaciukas)
    kates = session.query(Mama).all()
    for kate in kates:
        print(kate.id, kate.vardas, kate.veislynas, kate.gimimo_data, kate.kilmes_salis, kate.lytis)
    kates = input("Pasirinkite kates ID: ")
    kate.vaikai.append(gimes_kaciukas)
    session.add(gimes_kaciukas)
    session.commit()
    print(gimes_kaciukas)
    return gimes_kaciukas

def katinu_sarasas():
    print("--- Katinu sarasas ---")
    katinai = session.query(Tevas).all()
    for katinas in katinai:
        print(katinas.id, katinas.vardas, katinas.veislynas, katinas.gimimo_data, katinas.kilmes_salis, katinas.lytis)

def kaciu_sarasas():
    print("--- Kaciu sarasas ---")
    kates = session.query(Mama).all()
    for kate in kates:
        print(kate.id, kate.vardas, kate.veislynas, kate.gimimo_data, kate.kilmes_salis, kate.lytis)

def kaciuku_sarasas():
    print("--- Kaciuku sarasas ---")
    kaciukai = session.query(Vaikas).all()
    for kaciukas in kaciukai:
        print(kaciukas.id, kaciukas.vardas, kaciukas.veislynas, kaciukas.gimimo_data, kaciukas.kilmes_salis, kaciukas.lytis, kaciukas.tevas_id, kaciukas.mama_id)

#def bendra_paieska(query=session.query(Vaikas)):
    #kaciukai = session.query(Vaikas).all()
    #for kaciukas in kaciukai:
        #print(kaciukas)
    #paieska = input("Iveskite ko ieskote : ")
    #if not paieska:
        #return
    #try:
        #query_isvyko_gyventi = str(paieska)
    #except TypeError:
        #query = query.filter(Vaikas.lytis.ilike(f"{paieska}"))
    #else:
        #query = query.filter(Vaikas.isvyko_gyventi.ilike(f"{paieska}"))
    #finally:
        #kaciuku_sarasas(query)
        #if len(query.all()) > 0:
            #bendra_paieska(query)
        #else:
            #bendra_paieska()
     
    #print(paieska)
    #return bendra_paieska()
    
def pakeisti_irasa(query=session.query(Vaikas)):
    kaciukai = session.query(Vaikas).all()
    for kaciukas in kaciukai:
        print(kaciukas)
    keiciamo_id = int(input("Pasirinkite keiciamo kaciuko ID : "))
    keiciamas_kaciukas = session.query(Vaikas).get(keiciamo_id)
    paieska = input("Pasirinkite ka norite keisti: \n1-kaciuko lyti \n2-kaciuko varda \nJusu pasirinkimas: ")
    if paieska == "1":
        keiciamas_kaciukas.lytis = input("Iveskite nauja lyti: ")
    if paieska == "2":
        keiciamas_kaciukas.vardas = input("Iveskite nauja varda: ")
    session.commit()
    print(keiciamas_kaciukas)

def panaikinti_irasa():
    kaciukai = session.query(Vaikas).all()
    for kaciukas in kaciukai:
        print(kaciukas)
    trinamo_id = int(input("Psirinkite trinamo kaciuko ID : "))
    trinamas_kaciukas = session.query(Vaikas).get(trinamo_id)
    print("--- Irasas istrintas ---")
    session.delete(trinamas_kaciukas)
    session.commit()   


while True:
    pasirinkimas = naudotojo_meniu()
    if pasirinkimas == "O" or pasirinkimas == "":
        break
    if pasirinkimas == "1":
        prideti_katina()
    if pasirinkimas == "2":
        prideti_kate()
    if pasirinkimas == "3":
        prideti_kaciuka()
    if pasirinkimas == "4":
        katinu_sarasas()
    if pasirinkimas == "5":
        kaciu_sarasas()
    if pasirinkimas == "6":
        kaciuku_sarasas()
    #if pasirinkimas == "7":
        #bendra_paieska()
    if pasirinkimas == "8":
        pakeisti_irasa()
    if pasirinkimas == "9":
        panaikinti_irasa()


    