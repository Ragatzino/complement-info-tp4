import unittest
from service.compte_service import CompteService
from dao.compte_dao import CompteDao

"""Unitest"""

class TestCompte(unittest.TestCase):

    def test_creer_compte(self):
        compte_service = CompteService()
        compte_dao = CompteDao()
        compte = compte_service.creer_compte('TestPseudo', 'MotDePassePseudo')
        if compte.id:
            compte_dao.delete(compte)
        self.assertGreaterEqual(compte.id,0)

    def test_valid_pseudo_connu(self):
        compte_service = CompteService()
        compte_dao = CompteDao()
        compte = compte_service.creer_compte('TestPseudo', 'MotDePassePseudo')
        dispo = compte_service.pseudo_disponible('TestPseudo')
        compte_dao.delete(compte)
        self.assertFalse(dispo)

    def test_valid_pseudo_inconnu(self):
        compte_service = CompteService()
        dispo = compte_service.pseudo_disponible('PseudoFantaisiste')
        self.assertTrue(dispo)

if __name__ == '__main__':
    unittest.main()
