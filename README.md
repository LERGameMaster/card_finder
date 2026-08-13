# card_finder

Jeu de memoire dans le navigateur : retournez les cartes deux par deux et
retrouvez toutes les paires du set Blurness 3 avant que le chrono ne devienne
trop lourd.

HTML, CSS et JavaScript uniquement. Pas de backend, pas de framework, pas
d'etape de build, aucune requete reseau.

## Lancer une partie

Ouvrez `index.html` dans un navigateur : double-clic sur le fichier suffit.

Si vous preferez un serveur local (facultatif) :

```bash
python -m http.server 8000
```

puis <http://localhost:8000>.

## Regles

1. Choisissez un niveau : Facile (6 paires), Normal (10 paires) ou
   Difficile (18 paires).
2. Cliquez sur deux cartes pour les retourner.
3. Deux cartes identiques restent visibles et sont marquees en vert.
4. Sinon elles se retournent apres une seconde.
5. La partie s'arrete quand toutes les paires sont trouvees.

## Score

| Evenement | Points |
| --- | --- |
| Paire trouvee | +100 |
| Paire ratee | -10 |
| Bonus de temps | jusqu'a +200 |

Le bonus vaut 200 points tant que la partie tient sous le temps cible du
niveau (45 s, 90 s ou 180 s), puis decroit jusqu'a zero au double de ce
temps. Le meilleur score de chaque niveau est conserve dans le
`localStorage` du navigateur.

## Organisation du depot

| Fichier | Role |
| --- | --- |
| `index.html` | structure de la page et panneau de fin de partie |
| `css/style.css` | mise en page, grille et animation de retournement |
| `js/data.js` | liste des cartes et chemin du dos de carte |
| `js/game.js` | tirage, plateau, chrono, score et records |
| `assets/cards/` | visuels des cartes |
| `assets/card-back.webp` | dos de carte |
| `docs/NOTES.md` | notes de conception et retours de playtest |
