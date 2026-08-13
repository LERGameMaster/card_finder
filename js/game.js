/* Card Finder - construction du plateau.

   Aucun backend : les cartes viennent de js/data.js et tout se passe dans
   le navigateur. */

const NIVEAUX = {
  facile: { libelle: "Facile", paires: 6, colonnes: 4, colonnesMobile: 3 },
  normal: { libelle: "Normal", paires: 10, colonnes: 5, colonnesMobile: 4 },
  difficile: { libelle: "Difficile", paires: 18, colonnes: 6, colonnesMobile: 4 },
};

const plateau = document.querySelector("#plateau");
const selectDifficulte = document.querySelector("#difficulte");

let niveau = NIVEAUX.normal;
let cases = [];

function melanger(liste) {
  const copie = liste.slice();
  for (let i = copie.length - 1; i > 0; i -= 1) {
    const j = Math.floor(Math.random() * (i + 1));
    [copie[i], copie[j]] = [copie[j], copie[i]];
  }
  return copie;
}

function tirerCartes(nombre) {
  return melanger(CARTES).slice(0, nombre);
}

function construirePaquet(niveauChoisi) {
  const tirage = tirerCartes(niveauChoisi.paires);
  const paquet = [];

  tirage.forEach(function (carte) {
    paquet.push({ carte: carte, trouvee: false, retournee: false });
    paquet.push({ carte: carte, trouvee: false, retournee: false });
  });

  return melanger(paquet);
}

function gabaritCase(element, index) {
  return `
    <button type="button" class="case" data-index="${index}" aria-label="Carte face cachee">
      <span class="case__interieur">
        <span class="case__face case__face--dos">
          <img src="${DOS_DE_CARTE}" alt="">
        </span>
        <span class="case__face case__face--avant">
          <img src="${element.carte.image}" alt="${element.carte.nom}">
        </span>
      </span>
    </button>
  `;
}

function dessinerPlateau() {
  plateau.style.setProperty("--colonnes", niveau.colonnes);
  plateau.style.setProperty("--colonnes-mobile", niveau.colonnesMobile);
  plateau.innerHTML = cases.map(gabaritCase).join("");
}

function nouvellePartie() {
  niveau = NIVEAUX[selectDifficulte.value] || NIVEAUX.normal;
  cases = construirePaquet(niveau);
  dessinerPlateau();
}

document.addEventListener("DOMContentLoaded", nouvellePartie);
