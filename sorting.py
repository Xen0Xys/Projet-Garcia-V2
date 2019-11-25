"""
Etapes:
Rassembler les equipes
Composer les poules

"""
class IntegrityError(Exception):
    """Raised when list's integrity was not guaranted"""
    pass

class SortingAlgorithmV2():
    def __init__(self, _list):
        pass
    def doTraitment(self, _list):
        print("[INFO] : Starting traitment. (doTraitment function in SortingAlgorithmV2 class)")
        teams =  self.doTeams(_list)
        teams_nbre = self.countTeams(teams)
        if teams_nbre % 2 == 0:
            hens_nbre = teams_nbre / 2
        else:
            hens_nbre = (teams_nbre - 1) / 2 #Hens + 1 team
    def checkListIntegrity(self, _lists):
        print("[INFO] : Checking list integrity. (checkListIntegrity function in SortingAlgorithmV2 class)")
        keys = ["id", "last_name", "first_name", "name_establishment", "team_number", "license_number"]
        for part in _lists:
            try:
                for key in keys:
                    part[key]
                part_key_nbre = len(part.keys())
                keys_type_nbre = len(keys)
                if part_key_nbre != keys_type_nbre:
                    print("[WARNING] : {} keys give, only {} required. (checkListIntegrity function in SortingAlgorithmV2 class)".format(part_key_nbre, keys_type_nbre))
            except KeyError:
                print("[ERROR] : KeyError except, raised IntegrityError. (doTraitment function in SortingAlgorithmV2 class)")
                raise IntegrityError
    def doTeams(self, _list):
        print("[INFO] : Starting traitment. (doTraitment function in SortingAlgorithmV2 class)")
        def listEstablishments(_list):
            print("[INFO] : Listing establishments. (listEstablishments function in doTraitment function in SortingAlgorithmV2 class)")
            estab_list = []
            for player in _list:
                if player[""] not in estab_list: #Definir une fonction avec un seuil d'acceptation
                    estab_list.append(player[""])
            return estab_list
        def determinMaxTeamsByEstablishment(_list, _estab_list):
            print("[INFO] : Determine max teams by establishments. (determinMaxTeamsByEstablishment function in doTraitment function in SortingAlgorithmV2 class)")
            numbers = {}
            to_return = {}
            for estab in _estab_list:
                numbers[estab] = [0]
            for player in _list:
                try:
                    numbers[player["name_establishment"]][player["team_number"]] += 1
                except IndexError:
                    while len(numbers[player["name_establishment"]]) < [player["team_number"]]:
                        numbers[player["name_establishment"]].append[0]
                    numbers[player["name_establishment"]][player["team_number"]] += 1
            for estab_name in numbers.keys():
                to_return[estab_name] = len(numbers[estab_name])
            return to_return

        estab_list = listEstablishments(_list)
        teams = {}
        estab_nbre = determinMaxTeamsByEstablishment(_list, estab_list)
        for estab_name in estab_nbre.keys(): #setup good numbers of lists in each "teams" indexs
            teams[estab_name] = []
            for _ in len(estab_nbre[estab_name]):
                teams[estab_name].append([])
        for player in _list:
            teams[player["name_establishment"]][player["team_number"]].append(player)
        return teams
    def countTeams(self, _teams_list):
        print("[INFO] : Counting team's total number. (countTeams function in SortingAlgorithmV2 class)")
        teams_nbre = 0
        for estab_name in _teams_list.keys():
            teams_nbre += len(_teams_list[estab_name])
        return teams_nbre
    def composeTeamsFormat(self, _teams_nbre):
        pass
    def doHens(self, _teams_list):
        pass

        


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
    raise IntegrityError
    list = ["a", "b"]
    s_a_object = SortingAlgorithm(list)