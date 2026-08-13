# Notes de conception

## Regles retenues

- Le joueur retourne deux cartes par tour, au clic.
- Une paire trouvee reste visible jusqu'a la fin de la partie, encadree en
  vert et desactivee.
- Une paire ratee se retourne apres 850 ms : assez pour memoriser, assez
  court pour ne pas casser le rythme.
- La partie se termine quand toutes les paires sont trouvees ; le panneau de
  fin recapitule temps, coups et score.

## Equilibrage

| Niveau | Paires | Colonnes | Temps cible |
| --- | --- | --- | --- |
| Facile | 6 | 4 | 45 s |
| Normal | 10 | 5 | 90 s |
| Difficile | 18 | 6 | 180 s |

Le bonus de temps vaut 200 points sous le temps cible du niveau, puis
decroit lineairement jusqu'a zero au double de ce temps. Le temps cible est
indexe sur le niveau, contrairement a la premiere version ou il etait fixe.

## Rendu

- Le retournement utilise une rotation 3D en CSS (`transform-style:
  preserve-3d`), sans librairie.
- Le plateau est une grille CSS dont le nombre de colonnes est pilote par la
  variable `--colonnes`, remplacee par `--colonnes-mobile` sous 760 px.
- Les visuels sont des `.webp` d'environ 30 Ko : le jeu se charge vite et
  fonctionne hors ligne une fois la page ouverte.

## Pistes

- Apercu de deux secondes en debut de partie.
- Mode compte a rebours.
- Tableau des records par niveau affiche sur la page.
