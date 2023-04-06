# Otuspeli

Fuksikoodit 2022 peli, jossa huolehditaan otuksesta.

Aloitettu yhdessä Heljän, Elinan ja Macabren kanssa :D

Jatkettu jälkikäteen hieman

## Pelin pyöritys

Lataa tiedosto esim zippinä ja unzippaa, tai kloonaamalla repo gitillä (googlaa `git clone` tai tarkista esim [Lapion materiaalista](https://tkt-lapio.github.io/git/).

Toimii komentoriviltä, aja `python3 index.py` projektin juurikansiossa.

## Nykytoiminnallisuudet

- otuksen voi nimetä pelin alussa
- otuksella on nimi ja 2 statusta:
  - masu: nälän määrä
  - viba: olotila
- ruokkiminen vähentää nälkää
- leikkiminen lisää nälkää ja kohentaa olotilaa paljon
- otus voi kuolla (vain nälkään)


## Bugit
- (kirjaa tänne kun löytyy)

## TODO:

- otuksen nälkävaihtelu jne isommaksi (nyt maksimi vain 3)
- ASCII-otus ja sille ilmeet
- nimen hyödyntäminen peliteksteissä
- otukselle elinaika
- pelitilan tallennus
- minipelejä?
  - työt (ehkä raha)
  - lenkittäminen
      - satunnaistapahtumia
- myös mm. funktioiden erittely, funktionimien selkeytys jne


Muita asioita:
- eri lemmikkivaihtoehtoja?
- otukselle oma catchphrase/hokema (vapaavalintainen?)
- eri persoonallisuuksia
- rahaominaisuus?
- pelin loppuminen (osittain toteutettu)
  - eläimen kuoleminen
    - status liian pitkään huono
    - (pieni todennäköisyys että herää zombina ==> peli ei lopu)
  - otus karkaa 
    - voiko palata?
    - voi jäädä auton alle?
  - iso rahamäärä => eläke?