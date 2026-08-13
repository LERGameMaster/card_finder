# card_finder

Jeu de memoire en console : retournez les cartes deux par deux et retrouvez
toutes les paires avant que le chrono ne devienne trop lourd.

## Lancer une partie

```bash
python main.py
```

Aucune dependance externe, uniquement la bibliotheque standard de Python
(3.8+). Le jeu tourne aussi dans un executeur Python en ligne (repl.it,
programiz, ...) : copiez les fichiers `.py` et, si vous voulez la banniere,
le dossier `assets/`.

## Regles

1. Choisissez un niveau : Facile (6 paires), Normal (10 paires) ou
   Difficile (18 paires).
2. A chaque tour, saisissez les deux cases a retourner sur la meme ligne,
   par exemple `a1 b3`.
3. Une paire correcte reste affichee entre crochets, `[VDL]`.
4. Une paire incorrecte est retournee immediatement.
5. Tapez `q` pour abandonner la partie.

## Score

| Evenement | Points |
| --- | --- |
| Paire trouvee | +100 |
| Paire ratee | -10 |
| Bonus de temps | jusqu'a +200 |

Le bonus vaut 200 points tant que la partie tient sous deux minutes, puis
decroit jusqu'a zero a quatre minutes. Le chrono ne s'arrete pas pendant
l'affichage des resultats intermediaires.

## Organisation du depot

| Fichier | Role |
| --- | --- |
| `main.py` | menu, boucle de jeu, resume de fin de partie |
| `board.py` | grille, melange, coordonnees et rendu ASCII |
| `cards.py` | catalogue des cartes et tirage aleatoire |
| `levels.py` | definition des niveaux de difficulte |
| `scoring.py` | chronometre et calcul du score |
| `art.py` | chargement des visuels du dossier `assets/` |
| `docs/NOTES.md` | notes de conception et retours de playtest |

## Tests

```bash
python -m unittest discover -s tests
```
