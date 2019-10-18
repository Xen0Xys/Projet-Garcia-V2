class SortingAlgorithm():
    def __init__(self, *_lists):
        self.to_return = []
        for list in _lists:
            res = self.doTraitment(list)
            if res != "Error":
                self.to_return.append(res)
    def doTraitment(self, _list):
        if self.checkListIntegrity(_list) != "Error":
            return "Error" #Here do splits and traitment
        else: return "Error"
    def checkListIntegrity(self, _lists):
        for part in _lists:
            try:
                part["id"]
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
        categories = {""}


if __name__ == "__main__":
    list = ["a", "b"]
    s_a_object = SortingAlgorithm(list)