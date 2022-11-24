#!/usr/bin/env python
# -*- coding: utf-8 -*- 
print('Tervetuloa Otuspeliin :DD jeee')

otus = "( u w u )"
masu = 3

print(f"Täs on sulle otus, pidä siitä huolta. ==> {otus}")

vastaus = input("Anna otukselle ruokaa kirjoittamalla mitä tahansa paitsi pelkkä 0 :D")

if vastaus == "0":
  print(":(( Otus kuoli")
  print("(x__x)")
  quit() #ehkä näin?
else:
  masu += 1

print("Jee otus elää!")
print("( u w u )")

# okei en osaa jos on muuttuja jonka vaihdan falseksi :DDD


# while True:
#   vastaus = input("Haluatko että peli jatkuu? y/n ")
#   print("vastaus", vastaus)
#   if vastaus == "n":
#     break