class SortingAlgorithm():
    def __init__(self, *_lists):
        for list in _lists:
            self.doTraitment(list)
    def doTraitment(self, _list):
        if not self.checkListIntegrity(_list):
            pass
    def checkListIntegrity(self, _lists):
        for part in _lists:
            try:
                part["id"]
                #....
            except KeyError:
                return None
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
        def listEstablishment(_list):
            estab_list = []
            for part in _list:
                if part["establishment"] not in estab_list:
                    estab_list.append(part["establishment"])
            return estab_list
        estab_list = listEstablishment(_list)


if __name__ == "__main__":
    list = ["a", "b"]
    s_a_object = SortingAlgorithm(list)