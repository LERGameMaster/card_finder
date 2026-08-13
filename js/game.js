/* Card Finder - plateau et logique de jeu.

   Aucun backend : les cartes viennent de js/data.js et tout se passe dans
   le navigateur. */

const NIVEAUX = {
  facile: { libelle: "Facile", paires: 6, colonnes: 4, colonnesMobile: 3 },
  normal: { libelle: "Normal", paires: 10, colonnes: 5, colonnesMobile: 4 },
  difficile: { libelle: "Difficile", paires: 18, colonnes: 6, colonnesMobile: 4 },
};

const DELAI_RETOUR = 850;

const plateau = document.querySelector("#plateau");
const selectDifficulte = document.querySelector("#difficulte");
const boutonNouvelle = document.querySelector("#nouvelle-partie");
const zoneMessage = document.querySelector("#message");
const compteurPaires = document.querySelector("#paires");

let niveau = NIVEAUX.normal;
let cases = [];
let selection = [];
let pairesTrouvees = 0;
let plateauBloque = false;

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

function elementDeCase(index) {
  return plateau.querySelector('[data-index="' + index + '"]');
}

function majCompteurs() {
  compteurPaires.textContent = pairesTrouvees + " / " + niveau.paires;
}

function annoncer(texte, succes) {
  zoneMessage.textContent = texte;
  zoneMessage.classList.toggle("message--succes", !!succes);
}

function retourner(index) {
  const element = cases[index];
  element.retournee = true;
  const bouton = elementDeCase(index);
  bouton.classList.add("case--retournee");
  bouton.setAttribute("aria-label", element.carte.nom);
}

function cacher(index) {
  const element = cases[index];
  element.retournee = false;
  const bouton = elementDeCase(index);
  bouton.classList.remove("case--retournee");
  bouton.setAttribute("aria-label", "Carte face cachee");
}

function marquerTrouvee(index) {
  cases[index].trouvee = true;
  const bouton = elementDeCase(index);
  bouton.classList.add("case--trouvee");
  bouton.disabled = true;
}

function resoudre() {
  const [premier, second] = selection;
  const memeCarte = cases[premier].carte.id === cases[second].carte.id;

  if (memeCarte) {
    marquerTrouvee(premier);
    marquerTrouvee(second);
    pairesTrouvees += 1;
    majCompteurs();
    annoncer("Paire trouvee : " + cases[premier].carte.nom, true);
    selection = [];
    return;
  }

  plateauBloque = true;
  annoncer("Rate, les cartes sont retournees.");

  window.setTimeout(function () {
    cacher(premier);
    cacher(second);
    selection = [];
    plateauBloque = false;
  }, DELAI_RETOUR);
}

function jouer(index) {
  const element = cases[index];
  if (plateauBloque || element.trouvee || element.retournee) {
    return;
  }

  retourner(index);
  selection.push(index);

  if (selection.length === 2) {
    resoudre();
  }
}

function nouvellePartie() {
  niveau = NIVEAUX[selectDifficulte.value] || NIVEAUX.normal;
  cases = construirePaquet(niveau);
  selection = [];
  pairesTrouvees = 0;
  plateauBloque = false;

  dessinerPlateau();
  majCompteurs();
  annoncer("Cliquez sur deux cartes pour les retourner.");
}

plateau.addEventListener("click", function (evenement) {
  const bouton = evenement.target.closest(".case");
  if (bouton) {
    jouer(Number(bouton.dataset.index));
  }
});

boutonNouvelle.addEventListener("click", nouvellePartie);
selectDifficulte.addEventListener("change", nouvellePartie);

document.addEventListener("DOMContentLoaded", nouvellePartie);
