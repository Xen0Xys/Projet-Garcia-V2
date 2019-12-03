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
                    if all_data[j][1] != "":
                        t.append(all_data[j][i])
        to_return[all_data[0][i]] = t
    return to_return

def insertAllIntoDb(_dico, db):
    curs = db.cursor()
    lenght = len(_dico["Prénom"])
    for i in range(lenght):
        first_name = _dico["Prénom"][i]
        last_name = _dico["Nom"][i]
        team_number = _dico["N° équipe"][i]
        establishment = _dico["Nom étab."][i]
        curs.execute("INSERT INTO players VALUES(NULL, '{}', '{}', '{}', '{}');".format(first_name, last_name, team_number, establishment))
    curs.close()
    db.commit()
    db.close()


def getDataForSort():
    db = sqlite3.connect("database.db")
    curs = db.cursor()
    curs.execute("""SELECT id, first_name, last_name, establishment_name, team_number FROM players;""")
    res = curs.fetchall()
    to_return = []
    for player in res:
        player_dico = {}
        player_dico["id"] = int(player[0])
        player_dico["first_name"] = player[1]
        player_dico["last_name"] = player[2]
        player_dico["establishment_name"] = player[3]
        player_dico["team_number"] = int(player[4])
        to_return.append(player_dico)
    curs.close()
    db.close()
    return to_return

def verificationData(_data_in_css, _data_in_database):
    db = sqlite3.connect("database.db")
    curs = db.cursor()
    first_name = []
    last_name = []
    establishment_name = []
    team_number = []
    for i in range(len(_data_in_database)):
        first_name.append(_data_in_database[i]["first_name"])
        last_name.append(_data_in_database[i]["last_name"])
        establishment_name.append(_data_in_database[i]["establishment_name"])
        team_number.append(_data_in_database[i]["team_number"])

    if  first_name == _data_in_css["Prénom"]:
        print("le doc a les meme donne que la base de donné")
    else:
        for i in range (len(first_name)):
            if not first_name[i] == _data_in_css["Prénom"][i]:
                curs.close()
                db.close()
                uptdateDatabase(_data_in_css["Prénom"][i], _data_in_database[i], "prenom")


    if  first_name == _data_in_css["Nom"]:
        print("le doc a les meme donne que la base de donné")
    else:
        for i in range (len(last_name)):
            if not last_name[i] == _data_in_css["Nom"][i]:
                curs.close()
                db.close()
                uptdateDatabase(_data_in_css["Nom"][i], _data_in_database[i], "nom",)

    if  first_name == _data_in_css["N° équipe"]:
        print("le doc a les meme donne que la base de donné")
    else:
        for i in range (len(last_name)):
            if not last_name[i] == _data_in_css["N° équipe"][i]:
                db.close()
                uptdateDatabase(_data_in_css["N° équipe"][i], _data_in_database[i], "N° équipe",)

    if  first_name == _data_in_css["Nom étab."]:
        print("le doc a les meme donne que la base de donné")
    else:
        for i in range (len(last_name)):
            if not last_name[i] == _data_in_css["Nom étab."][i]:
                db.close()
                uptdateDatabase(_data_in_css["Nom étab."][i], _data_in_database[i], "Nom étab.",)


def uptdateDatabase(_data_uptdate, _data_in_database, column):
    os.remove("database.db")
    initDatabase()



def initDatabase():
    if not os.path.exists("database.db"):
        db = sqlite3.connect("database.db")
        curs = db.cursor()
        curs.execute('''CREATE TABLE "players" ("id" INTEGER NOT NULL UNIQUE, "first_name" VARCHAR(100) NOT NULL, "last_name" VARCHAR(100) NOT NULL, "team_number" VARCHAR(3) NOT NULL, "establishment_name" VARCHAR(100) NOT NULL, PRIMARY KEY("id" AUTOINCREMENT));''')
        db.commit()
        curs.close()
        insertAllIntoDb(deserializeAll("Feuille_de_match_Etablissement_2010.csv"), db)
    else:
        verificationData(deserializeAll("Feuille_de_match_Etablissement_2010.csv"), getDataForSort())



initDatabase()
    
