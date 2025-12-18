# Simulare 2D a difuziei termice

Acest proiect prezintă o simulare simplă a procesului de difuzie a căldurii într-un spațiu bidimensional. Scopul proiectului este de a ilustra cum se răspândește căldura de la zonele mai fierbinți către cele mai reci.

## Ce este difuzia
Difuzia termică reprezintă procesul prin care căldura se propagă în timp într-un material. În mod natural, energia termică se deplasează din zonele cu temperatură ridicată către zonele cu temperatură mai scăzută, până când se ajunge la un echilibru.

## Ideea simulării
Spațiul este reprezentat sub forma unei grile 2D, unde fiecare celulă are o valoare de temperatură. La fiecare pas al simulării, temperatura fiecărei celule este recalculată în funcție de temperaturile vecinilor săi direcți (sus, jos, stânga, dreapta).

O sursă de căldură este plasată inițial în centrul grilei, iar căldura se difuzează treptat către exterior.

## Modelul folosit
Temperatura unei celule este actualizată folosind o formulă discretizată simplă a ecuației difuziei:

T(i,j) ← T(i,j) + α · (vecini − 4 · T(i,j))

unde α este coeficientul de difuzie și controlează viteza cu care se propagă căldura.

## Funcționalități
- simulare numerică pe o grilă 2D
- animație a evoluției temperaturii
- reprezentare sub formă de hartă de culori
- butoane de pauză și reset
- schimbarea colormap-ului
- export opțional al simulării sub formă de GIF

## Structura proiectului
- `heat_diffusion_simulation.py` – versiunea finală a proiectului
- `versiune1.py` – implementare inițială
- `versiune2.py` – îmbunătățiri ale algoritmului
- `versiune3.py` – adăugarea animației
- `versiune4.py` – controale interactive
- `versiune5.py` – optimizări și rafinări
- `heat_diffusion.gif` – exemplu de animație generată

## Rulare
Simularea poate fi rulată folosind comanda:
```bash
python heat_diffusion_simulation.py
