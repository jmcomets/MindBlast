
import sys
sys.path.insert(0,'..')
from database import connect
from database.models import Product,Client,Reunion,Promotion, Feedback
import datetime
connect()

myClient=Client.objects(contact_id='003b000000KqjSFAAZ')

dateReuPassee=datetime.date(datetime.date.today().year,datetime.date.today().mounth, (datetime.date.today().day - 2) %7 ) 
dateFutur=datetime.date(datetime.date.today().year,datetime.date.today().mounth, (datetime.date.today().day + 3) %7 ) 

myReu=Reunion.objects(date=dateReuPassee,client=myClient)

feedbacks = [
#client avec maison propose assurance res sec
Feedback(positive=False,product=Product.objects.get(product_id='01tb0000001nUrwAAE'), client=Client.objects.get(contact_id='003b000000KqjSFAAZ')),
#client avec maison propose assurance res sec  
Feedback(positive=False,product=Product.objects.get(product_id='01tb0000001nUsBAAU'), client=Client.objects.get(contact_id='003b000000KqjSFAAZ')),
#client avec maison propose assurance res sec 
 Feedback(positive=False,product=Product.objects.get(product_id='01tb0000001nUsLAAU'), client=Client.objects.get(contact_id='003b000000KqjSFAAZ'))
]
myReu=Reunion.objects(date=dateReuPassee,client=myClient)
for fb in feedbacks:
	myReu.feedbacks.append(fb)