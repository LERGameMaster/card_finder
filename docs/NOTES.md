# Notes de conception

## Regles retenues

- Le joueur retourne deux cases par tour, en une seule saisie (`a1 b3`).
- Une paire trouvee reste visible jusqu'a la fin de la partie, entre crochets.
- Une paire ratee est immediatement retournee : pas de temporisation, le
  joueur voit les deux faces dans le rendu qui precede le message.
- La partie se termine quand toutes les paires sont trouvees, ou quand le
  joueur tape `q`.

## Equilibrage

| Niveau    | Paires | Colonnes | Duree cible |
| --- | --- | --- | --- |
| Facile    | 6      | 4        | 45 s        |
| Normal    | 10     | 5        | 90 s        |
| Difficile | 18     | 6        | 180 s       |

Le bonus de temps vaut 200 points tant que la partie tient sous 120 secondes,
puis decroit lineairement jusqu'a zero a 240 secondes. Il faudra sans doute
indexer cette cible sur le niveau plutot que la garder constante.

## Rendu console

- Trois caracteres par carte : au dela, la grille 6 colonnes ne tient plus
  dans un terminal de 80 colonnes.
- Les bordures sont partagees entre deux rangees pour gagner en hauteur.
- Les visuels ASCII vivent dans `assets/` et sont optionnels : le jeu doit
  rester jouable si seuls les `.py` sont copies dans un executeur en ligne.

## Pistes

- Sauvegarde du meilleur score par niveau.
- Mode compte a rebours.
- Affichage du nom complet des cartes deja appariees sous la grille.
