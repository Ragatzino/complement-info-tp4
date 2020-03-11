from service.compte_service import CompteService
from dao.compte_dao import CompteDao

compte_service = CompteService()
compte_dao = CompteDao()

"""Pytest"""

""" 
    assert verifie si la condition est vraie et fait en sorte que le programme s'arrête si la condition n'est pas vraie
"""
def test_creer_compte():
    compte = compte_service.creer_compte('TestPseudo', 'MotDePassePseudo')
    if compte.id:
        compte_dao.delete(compte)
    """ 
        assert verifie si l'id du compte a été créé
    """
    assert compte.id and compte.id > 0


def test_valid_pseudo_connu():
    compte = compte_service.creer_compte('TestPseudo', 'MotDePassePseudo')
    dispo = compte_service.pseudo_disponible('TestPseudo')
    compte_dao.delete(compte)
    """ 
           assert verifie si le compte est effectivement pas dispo
    """
    assert not(dispo)


def test_valid_pseudo_inconnu():
    dispo = compte_service.pseudo_disponible('PseudoFantaisiste')
    """ 
               assert verifie si le compte est effectivement dispo
    """
    assert dispo

if __name__ == "__main__":
    test_creer_compte()
    test_valid_pseudo_connu()
    test_valid_pseudo_inconnu()
    print("Everything passed")
