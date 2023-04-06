# Otuspeli

Fuksikoodit 2022 peli, jossa huolehditaan otuksesta.

Tehty yhdessä Heljän, Elinan ja Macabren kanssa :D gittiä ei tosin käytetty vaan google docsia :DDD

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
- 


## Bugit
- otus ei poistu kuollessa
  - tämän takia printataan edelleen positiiviset tekstit

## TODO:


- jos otus voi liian huonosti, se kuolee (esim. objekti poistetaan) ja peli loppuu
- ASCII-otus ja sille ilmeet
- nimen hyödyntäminen peliteksteissä
- otukselle elinaika
- pelitilan tallennus
- minipelejä?
  - työt (ehkä raha)
  - lenkittäminen
      - satunnaistapahtumia


Muita asioita:
- eri lemmikkivaihtoehtoja?
- otukselle oma catchphrase/hokema (vapaavalintainen?)
- eri persoonallisuuksia
- rahaominaisuus?
- pelin loppuminen
  - eläimen kuoleminen
    - status liian pitkään huono
    - (pieni todennäköisyys että herää zombina ==> peli ei lopu)
  - otus karkaa 
    - voiko palata?
    - voi jäädä auton alle?
  - iso rahamäärä => eläke?