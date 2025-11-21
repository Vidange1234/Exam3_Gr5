import pytest
import datetime
from rich.repr import Result

from Q2 import afficher_jours_examens


def test_afficher_jours_1():
    #arrange
    horaire_examen = {
        "math": "10/12/2015",
        "anglais": "12/12/2025",
        "français": "15/12/2025"

    }
    resultat_attendu=["jeudi", "vendredi", "lundi"]
    #act
    resultat = afficher_jours_examens(horaire_examen)
    #assert
    assert resultat == resultat_attendu
def test_afficher_jours2():
    #act
    horaire_examen = {}
    resultat_att = []
    
    
   
