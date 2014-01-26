
import sys
sys.path.insert(0,'..')
from database import connect
from database.models import Product,Client,Reunion, Feedback, Discount
import datetime
connect()

myClient=Client.objects.get(contact_id='003b000000KqjSFAAZ')

dateReuPassee=datetime.date(datetime.date.today().year,datetime.date.today().month, (datetime.date.today().day - 2) %7 ) 
dateFutur=datetime.date(datetime.date.today().year,datetime.date.today().month, (datetime.date.today().day + 3) %7 ) 

myReu=Reunion.objects.create(date=dateReuPassee,client=Client.objects.get(contact_id='003b000000KqjSFAAZ'), feedbacks=None)

feedbacks = [
#client avec maison propose assurance res sec
Feedback.objects.create(positive=False,product=Product.objects.get(product_id='01tb0000001nUrwAAE'), client=Client.objects.get(contact_id='003b000000KqjSFAAZ')),
#client avec maison propose assurance res sec  
Feedback.objects.create(positive=False,product=Product.objects.get(product_id='01tb0000001nUsBAAU'), client=Client.objects.get(contact_id='003b000000KqjSFAAZ')),
#client avec maison propose assurance res sec 
 Feedback.objects.create(positive=True,product=Product.objects.get(product_id='01tb0000001nUsLAAU'), client=Client.objects.get(contact_id='003b000000KqjSFAAZ'))
]
myReu=Reunion.objects.create(date=dateReuPassee,client=myClient)
for fb in feedbacks:
	myReu.feedbacks.append(fb)

prod=Product.objects.get(product_id='01tb0000001nUrwAAE')

disc = Discount.objects.create(products=[], description="30 % de remise sur ce produit si le client a moins de 25 ans !")
disc.products.append(prod)