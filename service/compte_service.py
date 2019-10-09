from dao.compte_dao import CompteDao
from business_model.compte import Compte


class CompteService:
    compte_dao = CompteDao()

    def pseudo_disponible(self, pseudo):
        return not(CompteService.compte_dao.find_by_pseudo(pseudo))

    def creer_compte(self, pseudo, motdepasse):
        compte = Compte(pseudo, motdepasse)
        return CompteService.compte_dao.create(compte)
