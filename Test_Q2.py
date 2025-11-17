import pytest
import datetime
from rich.repr import Result

from Q2 import afficher_jours_examens


def test_afficher_jours_examens(horaire_examen):
    horaire_examen = {
        "math": "10/12/2015",
        "anglais": "12/12/2025",
        "français": "15/12/2025"

    }
    resultat_attendu="jeudi", "vendredi", "lundi"
    assert afficher_jours_examens(horaire_examen) == resultat_attendu
    assert date = datetime.datetime.strptime(horaire_examen[examen], "%d/%m/%Y")
