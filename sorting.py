import database

"""
Etapes:
Rassembler les equipes
Composer les poules

"""
class IntegrityError(Exception):
    """Raised when list's integrity was not guaranted"""
    pass

class SortingAlgorithm():
    def __init__(self, t=""):
        pass
    def doTraitment(self):
        print("[INFO] : Initializing database. (doTraitment function in SortingAlgorithm class)")
        database.initDatabase()
        print("[INFO] : Getting data from database. (doTraitment function in SortingAlgorithm class)")
        _list = database.getDataForSort()
        self.checkListIntegrity(_list)
        print("[INFO] : Starting traitment. (doTraitment function in SortingAlgorithm class)")
        teams =  self.doTeams(_list)
        #teams_nbre = self.countTeams(teams)
        flat_teams_list = self.flattenTeamsList(teams)
        hens_1, hens_2 = self.doHens(flat_teams_list)
        for team in hens_1:
            for player in team:
                print(player)
        print("[INFO] : Traitment end, returning values. (doTraitment function in SortingAlgorithm class)")
    def checkListIntegrity(self, _lists):
        print("[INFO] : Checking list integrity. (checkListIntegrity function in SortingAlgorithm class)")
        keys = ["id", "last_name", "first_name", "name_establishment", "team_number"]
        for part in _lists:
            try:
                for key in keys:
                    part[key]
                part_key_nbre = len(part.keys())
                keys_type_nbre = len(keys)
                if part_key_nbre != keys_type_nbre:
                    print("[WARNING] : {} keys give, only {} required. (checkListIntegrity function in SortingAlgorithm class)".format(part_key_nbre, keys_type_nbre))
            except KeyError:
                print("[ERROR] : KeyError except, raised IntegrityError. (checkListIntegrity function in SortingAlgorithm class)")
                raise IntegrityError
    def doTeams(self, _list):
        print("[INFO] : Doing Teams. (doTeams function in SortingAlgorithm class)")
        def listEstablishments(_list):
            print("[INFO] : Listing establishments. (listEstablishments function in doTraitment function in SortingAlgorithm class)")
            estab_list = []
            for player in _list:
                if player["name_establishment"] not in estab_list: #Definir une fonction avec un seuil d'acceptation
                    estab_list.append(player["name_establishment"])
            return estab_list
        def determinMaxTeamsByEstablishment(_list, _estab_list):
            print("[INFO] : Determining max teams by establishments. (determinMaxTeamsByEstablishment function in doTraitment function in SortingAlgorithm class)")
            numbers = {}
            to_return = {}
            for estab in _estab_list:
                numbers[estab] = [0]
            for player in _list:
                try:
                    numbers[player["name_establishment"]][(player["team_number"]) - 1] += 1
                except IndexError:
                    while len(numbers[player["name_establishment"]]) < player["team_number"]:
                        numbers[player["name_establishment"]].append(0)
                    numbers[player["name_establishment"]][(player["team_number"]) - 1] += 1
            for estab_name in numbers.keys():
                to_return[estab_name] = len(numbers[estab_name])
            return to_return
        estab_list = listEstablishments(_list)
        teams = {}
        estab_nbre = determinMaxTeamsByEstablishment(_list, estab_list)
        for estab_name in estab_nbre.keys(): #setup good numbers of lists in each "teams" indexs
            teams[estab_name] = []
            for _ in range(estab_nbre[estab_name]):
                teams[estab_name].append([])
        for player in _list:
            teams[player["name_establishment"]][(player["team_number"]) - 1].append(player)
        return teams
    def countTeams(self, _teams_list):
        print("[INFO] : Counting team's total number. (countTeams function in SortingAlgorithm class)")
        teams_nbre = 0
        for estab_name in _teams_list.keys():
            teams_nbre += len(_teams_list[estab_name])
        return teams_nbre
    def flattenTeamsList(self, _teams_list):
        print("[INFO] : Flatten teams least. (flattenTeamsList function in SortingAlgorithm class)")
        flat_teams_list = []
        for estab in _teams_list.keys():
            for team in _teams_list[estab]:
                flat_teams_list.append(team)
        return flat_teams_list
    def doHens(self, _flat_teams_list):
        print("[INFO] : Doing hens. (doHens function in SortingAlgorithm class)")
        hens_1 = []
        hens_2 = []
        for i in range(len(_flat_teams_list)):
            if i % 2 == 0:
                hens_1.append(_flat_teams_list[i])
            else:
                hens_2.append(_flat_teams_list[i])
        return hens_1, hens_2
    def doHensMatchs(self, _hens):
        pass
   


if __name__ == "__main__":
    sorting_object = SortingAlgorithm()
    sorting_object.doTraitment()
