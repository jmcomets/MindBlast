from settings import (db_name, db_host, db_port, db_user, db_pass)
import mongoengine

def connect():
    mongoengine.connect(db_name,
            host=db_host, port=db_port,
            username=db_user, password=db_pass)
