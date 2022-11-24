import bcolors
class Otus:

  #TODO:
  # ehkä joku minigame jolla voi nostaa vibaa tai nälkää halvalla?

  def __init__(self, nimi: str):
    self.nimi = nimi #inputtina niin on str? pitääks jotenkin validoida?
    self.masu = 3 #tarkoitus olla max 3?
    self.vibat = 3 #max 3
    # vois olla joku elossaolo-boolean ainakin jos voi epäkuolettaa otuksen
    
  def muuta_masu_statusta(self, maara):
    self.masu += maara
    # vaikka plussais miinusta niin silti miinustaa

  def masu_status(self):
    if self.masu == 1 or self.masu == 0:
       print(bcolors.FAIL + bcolors.BOLD + "Otuksella on näläkä. RUOKI >:(" + bcolors.ENDC)
    elif self.masu < 0:
        print("Otuksesi kuoli nälkään.")
        print(bcolors.BOLD + "Hävisit pelin." + bcolors.ENDC)
    elif self.masu == 2:
        print(bcolors.WARNING + "Otuksellasi on hyvät oltavat :)" + bcolors.ENDC)
        print(bcolors.WARNING + "Ei ole nälkä :)" + bcolors.ENDC)
  
    elif self.masu == 3:
        print(bcolors.OKGREEN + "Otuksesi on kylläinen" + bcolors.ENDC)
        print(bcolors.OKGREEN + bcolors.BOLD + "Otusta ei voi ruokkia enempää." + bcolors.ENDC)

  def muuta_vibat_statusta(self, maara):
    self.vibat += maara

  def vibat_status(self):
    if self.vibat == 1 or self.vibat == 0:
        print(bcolors.FAIL + bcolors.BOLD + "Otuksella on näläkä. RUOKI >:(" + bcolors.ENDC)
    elif self.vibat < 0:
        print("Otuksesi kuoli.")
        print(bcolors.BOLD + "Hävisit pelin." + bcolors.ENDC)
    elif self.vibat == 2:
        print(bcolors.WARNING + "Otuksellasi on hyvät oltavat :)" + bcolors.ENDC)
        print(bcolors.WARNING + "Ihan jees vibat :)" + bcolors.ENDC)
    elif self.vibat == 3:
        print(bcolors.OKGREEN + "Otuksesi on otuilee :3" + bcolors.ENDC)
        print(bcolors.OKGREEN + bcolors.BOLD + "Otus ei voi otuilla tämän enempää." + bcolors.ENDC)

  def leiki(self):
    # miinustaa masua =>
    self.muuta_masu_statusta(-1)
    self.muuta_vibat_statusta(1)

  def __str__(self):
    # olion status/olotila esim nälkästatus, vai olion sprite?
    # masu 2/3
    # vibes 1/3
    pass



### miina = Otus("Miina")

### miina.masuun_lisaa()

### miinanmasu = miina.masu
# gfdkjdk
# miina.masu = hjshfkdsj