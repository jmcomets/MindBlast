import settings
import mongoengine

def connect():
    mongoengine.connect(settings.db_name)
