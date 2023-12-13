class ChainUtils:
    @staticmethod
    def est_anagramme(chaine1, chaine2):
        up_chaine1 = chaine1.upper()
        up_chaine2 = chaine2.upper()
        if not len(up_chaine1) == len(up_chaine2):
            return False
        return sorted(up_chaine1) == sorted(up_chaine2)

    @staticmethod
    def comptage_chaine(chaine1, sous_chaine):
        return chaine1.count(sous_chaine)


print(ChainUtils.est_anagramme("chinee", "echine"))
print(ChainUtils.comptage_chaine("Le bâteau est dans l'eau", "eau"))
