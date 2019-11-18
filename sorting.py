"""
Etapes:
Rassembler les equipes
Composer les poules

"""
class SortingAlgorithmV2():
    def __init__(self):
        pass
    def checkListIntegrity(self, _lists):
        for part in _lists:
            try:
                if part["id"] == "":
                    return "Error"
                if part["category"] == "":
                    return "Error"
                #....
            except KeyError:
                return "Error"

class SortingAlgorithm():
    def __init__(self, *_lists):
        self.to_return = []
        for list in _lists:
            res = self.doTraitment(list)
            if res != "Error":
                self.to_return.append(res)
    def doTraitment(self, _list):
        if self.checkListIntegrity(_list) != "Error":
            exc, n_exc = self.splitByExcellencies(_list)
            """
            exc_splt_estab = self.splitByEstablishment(exc)
            n_exc_splt_estab = self.splitByEstablishment(n_exc)
            Not sure
            """
            exc_splt_cat = self.sortByCategory(exc)
            n_exc_splt_cat = self.sortByCategory(n_exc)
            return "Error" #Here do splits and traitment
        else: return "Error"
    def checkListIntegrity(self, _lists):
        for part in _lists:
            try:
                if part["id"] == "":
                    return "Error"
                if part["category"] == "":
                    return "Error"
                #....
            except KeyError:
                return "Error"
    def splitByExcellencies(self, _list):
        excellencies_list = []
        not_excellencies_list = []
        for part in _list:
            if part["excellencies"] == True:
                excellencies_list.append(part)
            else:
                not_excellencies_list.append(part)
        return excellencies_list, not_excellencies_list
    def splitByEstablishment(self, _list):
        splt_estab_list = {}
        def listEstablishment(_list):
            estab_list = []
            for part in _list:
                if part["establishment"] not in estab_list:
                    estab_list.append(part["establishment"])
            return estab_list
        estab_list = listEstablishment(_list)
        for key in estab_list:
            splt_estab_list[key] = []
            for part in _list:
                splt_estab_list[key].append(part)
        return splt_estab_list
    def sortByCategory(self, _list):
        categories = {"d_m": [], "d_g": [], "s_f": [], "s_g": [], "unknow": []}
        for part in _list:
            if part["category"] == "d_m":
                categories["d_m"].append(part)
            elif part["category"] == "d_g":
                categories["d_g"].append(part)
            elif part["category"] == "s_f":
                categories["s_f"].append(part)
            elif part["category"] == "s_g":
                categories["s_g"].append(part)
            else:
                categories["unknow"].append(part)
        return categories
    def sortByClassment(self, _category_list):
        for category in _category_list.key():
            if category != "unknow":
                pass
                #Do sort
    def doHen(self, _category_list, _hen_nbre):
        for category in _category_list.key():
            if category != "unknow":
                var_dir = 1

        


if __name__ == "__main__":
    list = ["a", "b"]
    s_a_object = SortingAlgorithm(list)