import sqlite3
import os


def deserializeAll(_file_name, db):
    fichier = open(_file_name, "r", encoding="utf8", errors='ignore')
    d = []
    a= fichier.read()
    b = a.split("\n")
    for i in range (len(b)):
        d.append([""])
        d[i] = b[i].split("\\")
    print(str(d[1][1]))

    curs = db.cursor()
    for i in range (len(d)-2):
        curs.execute("INSERT INTO players ( first_name, last_name, name_establishment, team_number, license_number)\
            VALUES ('str(d[1][1])', 'a', 'a', 'a','a')")
    curs.close()
    db.commit()


if not os.path.exists("database.db"):
    db = sqlite3.connect("database.db")
    curs = db.cursor()
    curs.execute('''CREATE TABLE "players" ("id" INTEGER NOT NULL UNIQUE, "first_name" VARCHAR(100) NOT NULL, "last_name" VARCHAR(100) NOT NULL, "name_establishment" VARCHAR(3) NOT NULL, "team_number" VARCHAR(100) NOT NULL,"license_number" VARCHAR(100) NOT NULL, PRIMARY KEY("id" AUTOINCREMENT));''')
    db.commit()
    curs.close()
    deserializeAll("Feuille_de_match_Etablissement_2010.csv", db)
