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
            if j != 0:
                t.append(all_data[j][i])
        to_return[all_data[0][i]] = t
    return to_return

def insertAllIntoDb(_dico, db):
    curs = db.cursor()
    lenght = len(_dico["NUM_LICENCE"])
    for i in range(lenght):
        first_name = _dico["PRENOM_LICENCE"][i]
        last_name = _dico["NOM_LICENCEE"][i]
        excellence = _dico["EXCELLENCE"][i]
        establishment = _dico["NOM_ETABLISSEMENT_ATTACHE"][i]
        curs.execute("INSERT INTO players VALUES(NULL, '{}', '{}', '{}', '{}')".format(first_name, last_name, excellence, establishment))
    curs.close()
    db.commit()

t1 = time.time()

if not os.path.exists("database.db"):
    db = sqlite3.connect("database.db")
    curs = db.cursor()
    curs.execute('''CREATE TABLE "players" ("id" INTEGER NOT NULL UNIQUE, "first_name" VARCHAR(100) NOT NULL, "last_name" VARCHAR(100) NOT NULL, "excellence" VARCHAR(3) NOT NULL, "establishment" VARCHAR(100) NOT NULL, PRIMARY KEY("id" AUTOINCREMENT));''')
    db.commit()
    curs.close()
    insertAllIntoDb(deserializeAll("LL.csv"), db)
    
t2 = time.time()
print(t2 - t1)