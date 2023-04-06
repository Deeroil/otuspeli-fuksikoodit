from Otus import Otus
#en tiedä onks tää oikeesti tarpeellista :D
#!/usr/bin/env python
# -*- coding: utf-8 -*- 
print('Tervetuloa Otuspeliin :DD jeee')

def luo_otus():
    nimi = input("Annappas otukselle nimi")
    return Otus(nimi)

def ohje():
   print("komennot: ")
   print("0 tapa otus")
   print("1 syötä otusta")
   print("2 leiki otuksen kanssa")
   print("3 tarkista otuksen vointi")
   print("4 lopeta peli")

otus = luo_otus()
ohje()
while True:
   print("")
   komento = input("komento: ")
   if komento == "0":
       print("(x__x)")
       print("Otus kuol :(")
       print("peli loppuu")
       quit()
   elif komento == "1" and otus.elossa:
       #kutsutaan tässä funktiota joka ruokkii otusta
       otus.muuta_masu_statusta(1)
       otus.masu_status()

       if (otus.vibat <= 1):
         otus.vibat_status()
   
   elif komento == "2" and otus.elossa:
       #kutsutaan tässä funktiota joka leikkii otuksen kanssa
      otus.leiki()
      print("Whii otuksella on kivaa :3")

      if (otus.masu <= 1):
        otus.masu_status()

   elif komento == "3":
       #kutsutaan tässä funktiota joka printtaa otuksen statsit
       print(vars(otus))
       otus.status()
    
   elif komento == "4":
      #  break #lopetetaan peli
      print("Peli loppui")
      quit()

   elif not otus.elossa:
      print("Otus on kuollut")
      vastaus = input("Luo uusi otus? y/n")
      if vastaus == "y":
         otus = luo_otus()
      elif vastaus == "n":
         print("Säilytettiin raato")
         ohje()

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