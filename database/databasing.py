import pymongo
from faker import Faker
from random import Random
import sys

sys.path.insert(0,"..")

if __name__=='__main__':

    f = Faker()
    r=Random()
    r.seed()

    mc= pymongo.MongoClient()
    db = mc["salesforce_add_db"]

    with open("contacts.txt", 'r') as file:
    


       ''' data=file.read()
        db.clients.update({"id_contact": (str)(data), "voiture": r.randint(0,1), "enfant": r.randint(0,1), "marie" : r.randint(0,1), "proprietaire" : r.randint(0,1)})
        
        nbre_max = r.randint(0,1000)
        db.challenges.update({"id_challenge":(str)(data)+'con', "titre": f.username(), "contrat": blabla, "avancement": r.randint(0,nbre_max), "nombre_total" :  nbre_max, "description": f.company()})

        # Les récupérer
        all_users = db.users.find()
        print all_users
        "french_users = db.users.find({"country": "France"})"'''




'''    conn = sqlite3.connect('salesforce.db')
    c=conn.cursor()

    c.execute('''DROP TABLE IF EXISTS clients''')
    c.execute('''DROP TABLE IF EXISTS challenges''')

    c.execute('''CREATE TABLE clients(id_contact unique, voiture integer, enfant integer, marie integer, proprietaire integer)''')
    c.execute('''CREATE TABLE challenges (id unique, id_challenge integer, titre text, contrat blob, avancement integer, nombre_total integer, description text)''')



open()
        c.execute("INSERT INTO clients VALUES ("(str)()+"),"+(str)(r.randint(0,1))+","+(str)(r.randint(0,1))+","+(str)(r.randint(0,1))+","+(str)(r.randint(0,1)))
        c.execute("INSERT INTO challenges VALUES (1000"+(str)(i)+"),"+(str)(r.randint(0,1))+","+(str)(r.randint(0,1))+","+(str)(r.randint(0,1))+","+(str)(r.randint(0,1)))'''