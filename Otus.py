class bcolors:
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'

class Otus:

  #TODO:
  # ehkä joku minigame jolla voi nostaa vibaa tai nälkää halvalla?

  def __init__(self, nimi: str):
    self.nimi = nimi #inputtina niin on str? pitääks jotenkin validoida?
    self.masu = 3 #tarkoitus olla max 3?
    self.vibat = 3 #max 3
    # vois olla joku elossaolo-boolean ainakin jos voi epäkuolettaa otuksen
    
  def muuta_masu_statusta(self, muutos: int):
    # Muutosten mahdolliset arvot: -1 (nälkä vähenee), 1 (olio syö jotain), 0 (ei muutosta)
    # Ruokatilat: 0, 1, 2, 3
    if self.masu >= 0 and muutos < 0:
       self.masu += muutos

    if self.masu >= 3 and muutos >= 0:
        pass
    
    if self.masu >= 0 and self.masu < 3 and muutos >= 0:
      if self.masu + muutos > 3:
        self.masu = 3

      if 0 <= (self.masu + muutos) <= 3:
        self.masu += muutos

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

  def muuta_vibat_statusta(self, muutos):
    if self.vibat >= 0 and muutos < 0:
       self.vibat += muutos

    if self.vibat >= 3 and muutos >= 0:
        pass
    
    if self.vibat >= 0 and self.vibat < 3 and muutos >= 0:
      if self.vibat + muutos > 3:
        self.vibat = 3

      if 0 <= (self.vibat + muutos) <= 3:
        self.vibat += muutos

  def vibat_status(self):
    if self.vibat == 1 or self.vibat == 0:
        print(bcolors.FAIL + bcolors.BOLD + "Otuksella on ihan kamala olo. LEIKI TAI KÄY HUONOSTI >:(" + bcolors.ENDC)
    elif self.vibat < 0:
        print("Otuksesi kuoli.")
        print(bcolors.BOLD + "Hävisit pelin." + bcolors.ENDC)
    elif self.vibat == 2:
        print(bcolors.WARNING + "Otuksellasi on hyvät oltavat :)" + bcolors.ENDC)
        print(bcolors.WARNING + "Ihan jees vibat :)" + bcolors.ENDC)
    elif self.vibat == 3:
        print(bcolors.OKGREEN + "Otuksesi otuilee :3" + bcolors.ENDC)
        print(bcolors.OKGREEN + bcolors.BOLD + "Otuksen viba ei voi olla tämän parempi." + bcolors.ENDC)

  def leiki(self):
    # miinustaa masua yhden, lisää vibaa paljon
    self.muuta_masu_statusta(-1)
    self.muuta_vibat_statusta(2)

  def status(self):
    self.masu_status()
    self.vibat_status()

  def __str__(self):
    # olion status/olotila esim nälkästatus, vai olion sprite?
    # masu 2/3
    # vibes 1/3
    return "emt string"