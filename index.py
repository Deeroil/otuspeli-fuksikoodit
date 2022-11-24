from Otus import Otus
#en tiedä onks tää oikeesti tarpeellista :D
#!/usr/bin/env python
# -*- coding: utf-8 -*- 
print('Tervetuloa Otuspeliin :DD jeee')

nimi = input("Annappas otukselle nimi")
otus = Otus(nimi)

def ohje():
   print("komennot: ")
   print("0 tapa olio")
   print("1 syötä oliota")
   print("2 lopeta peli")
   print("3 tarkista olion vointi")
 
#PÄÄOHEJLMA TAI JOTAIN esim vaikka joku suorita() komento
ohje()
while True:
   print("")
   komento = input("komento: ")
   if komento == "0":
       #kutsutaan tässä funktiota joka tappaa otuksen
       print("(x__x)")
       print("Otus kuol :(")
       print("peli loppuu")
       quit()
   elif komento == "1":
       #kutsutaan tässä funktiota joka ruokkii otusta
       otus.muuta_masu_statusta(1)
   elif komento == "2":
      #  break #lopetetaan peli
      print("Peli loppui")
      quit()
   elif komento == "3":
       #kutsutaan tässä funktiota joka printtaa otuksen statsit
       print(vars(otus))
   else:
       ohje()


#tulostaa kivasti jeee :D:D:D
#print(vars(otus))  

# otus = Otus("Otus")

# # print(otus)

# print("otus.masu ", otus.masu)
# print("otus.vibat ", otus.vibat)

# otus.muuta_masu_statusta(2)

# print("otus.masu ", otus.masu)

# otus.muuta_masu_statusta(-5)

# print("otus.masu ", otus.masu)

# print(f"Täs on sulle otus, pidä siitä huolta. ==> {otus}")

# vastaus = input("Anna otukselle ruokaa kirjoittamalla mitä tahansa paitsi pelkkä 0 :D")

# if vastaus == "0":
#   print(":(( Otus kuoli")
#   print("(x__x)")
#   quit() #ehkä näin?
# else:
#   masu += 1

# print("Jee otus elää!")
# print("( u w u )")

# okei en osaa jos on muuttuja jonka vaihdan falseksi :DDD


# while True:
#   vastaus = input("Haluatko että peli jatkuu? y/n ")
#   print("vastaus", vastaus)
#   if vastaus == "n":
#     break