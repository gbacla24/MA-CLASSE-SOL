"""Calcul de la moyenne pondérée d'un élève."""
import csv


def moyenne_ponderee(notes):
    """Retourne la moyenne sur 20, arrondie à 2 décimales.

    notes : liste de tuples (note, coefficient).
    """
    if not notes:
        raise ValueError("La liste de notes est vide")
    total = sum(note * coef for note, coef in notes)
    somme_coefs = sum(coef for _, coef in notes)
    return round(total / somme_coefs, 2)


def lire_notes(chemin):
    """Lit un fichier CSV (matiere,note,coefficient) et retourne la liste des tuples."""
    with open(chemin, newline="", encoding="utf-8") as fichier:
        lecteur = csv.DictReader(fichier)
        return [(float(l["note"]), float(l["coefficient"])) for l in lecteur]


if __name__ == "__main__":
    def mention(moyenne):
      """Renvoie la mention correspondant a une moyenne sur 20."""
      if moyenne >= 16:
        return "Tres bien"
      if moyenne >= 14:
        return "Bien"
      if moyenne >= 12:
        return "Assez bien"
      if moyenne >= 10:
        return "Passable"
      return "Insuffisant"
    notes = lire_notes("donnees/notes.csv")
    moyenne = moyenne_ponderee(notes)
    print("Moyenne :", moyenne)
    print("Mention :", mention(moyenne))
print("afficher la mention")
