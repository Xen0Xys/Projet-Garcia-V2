import sqlite3
import os
import time

def deserializeAll(_file_name):
    file = open(_file_name, "r", encoding="utf8", errors='ignore')
    ct = file.read()
    file.close()
    t1 = ct.split("\n")
    all_data = []
    for item in t1:
        all_data.append(item.split("\\"))
    to_return = {}
    for i in range(len(all_data[0])):
        t = []
        for j in range(len(all_data)):
            if len(all_data[j]) == 13:
                if j != 0:
                    print(all_data[j][i])
                    t.append(all_data[j][i])
        to_return[all_data[0][i]] = t
    return to_return

def insertAllIntoDb(_dico, db):
    curs = db.cursor()
    lenght = len(_dico["Prénom"])
    for i in range(lenght):
        first_name = _dico["Prénom"][i]
        last_name = _dico["Nom"][i]
        excellence = _dico["N° équipe"][i]
        establishment = _dico["Nom étab."][i]
        curs.execute("INSERT INTO players VALUES(NULL, '{}', '{}', '{}', '{}')".format(first_name, last_name, excellence, establishment))
    curs.close()
    db.commit()

os.remove("database.db")
if not os.path.exists("database.db"):
    db = sqlite3.connect("database.db")
    curs = db.cursor()
    curs.execute('''CREATE TABLE "players" ("id" INTEGER NOT NULL UNIQUE, "first_name" VARCHAR(100) NOT NULL, "last_name" VARCHAR(100) NOT NULL, "team_number" VARCHAR(3) NOT NULL, "establishment" VARCHAR(100) NOT NULL, PRIMARY KEY("id" AUTOINCREMENT));''')
    db.commit()
    curs.close()
    insertAllIntoDb(deserializeAll("Feuille_de_match_Etablissement_2010.csv"), db)
    