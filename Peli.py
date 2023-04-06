from Otus import Otus


class Peli:

    def __init__(self):
        self.otus = None

    def alku(self):
        print('Tervetuloa Otuspeliin :DD jeee')
        self.otus = self.luo_otus()
        self.ohje()

    def luo_otus(self):
        nimi = input("Annappas otukselle nimi: ")
        return Otus(nimi)

    def ohje(self):
        print("komennot: ")
        print("0 tapa otus")
        print("1 syötä otusta")
        print("2 leiki otuksen kanssa")
        print("3 tarkista otuksen vointi")
        print("4 lopeta peli")

    def suorita(self):
        while True:
            print("")
            komento = input("komento: ")
            if komento == "0":
                print("(x__x)")
                print("Otus kuol :(")
                print("peli loppuu")
                quit()

            elif komento == "1" and self.otus.elossa:
                # ruokkii otusta
                self.otus.muuta_masu_statusta(1)
                self.otus.masu_status()

                if (self.otus.vibat <= 1):
                    self.otus.vibat_status()

            elif komento == "2" and self.otus.elossa:
                # leikkii otuksen kanssa
                self.otus.leiki()
                print("Whii otuksella on kivaa :3")

                if (self.otus.masu <= 1):
                    self.otus.masu_status()

            elif komento == "3":
                # printtaa otuksen statsit
                print(vars(self.otus))
                self.otus.status()

            elif komento == "4":
                print("Peli loppui")
                quit()

            elif not self.otus.elossa:
                print("Otus on kuollut")
                vastaus = input("Luo uusi otus? (y/n) ")
                if vastaus == "y":
                    self.otus = self.luo_otus()
                elif vastaus == "n":
                    print("Säilytettiin raato")
                    self.ohje()

            else:
                self.ohje()
