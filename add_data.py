import random
# -*- coding: utf-8 -*-
from datetime import date, timedelta
import database; database.connect()
from database.models import *

if __name__ == '__main__':
    clients = list(Client.objects)
    random.shuffle(clients)
    products = list(Product.objects)
    for client in clients:
        today = date.today()
        reunion_date = today - timedelta(days=(today.weekday() - random.randint(0, 6)) % 7)
        reunion = Reunion(date=reunion_date, client=client)
        print 'Réunion le', reunion_date, 'avec', client.first_name, client.last_name
        print 'Caractéristiques:', client.boolean_attributes
        go = raw_input('Simuler ? (o/N)')
        if go != 'o':
            continue
        feedbacks = []
        for product in products:
            ok = raw_input('A-t-il aimé le produit "%s" ? (o/n/Ign)' % product.name.encode('utf-8'))
            if ok == 'o':
                ok = True
            elif ok == 'n':
                ok = False
            else:
                continue
            feedbacks.append(Feedback(positive=ok, product=product))
        for fb in feedbacks:
            reunion.feedbacks.append(fb)
            fb.client = client
            fb.save()
        reunion.save()
