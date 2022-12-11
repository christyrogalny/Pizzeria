import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pizzeria.settings")

import django
django.setup()

from pizzas.models import *


pizza = Pizza.objects.all()

#print(pizza)

p = Pizza.objects.get(id=1)
print(p)

toppings = Topping.objects.filter(pizza=p)

for t in toppings:
    print(t)
    print(t.date_added)

from django.contrib.auth.models import User

for user in User.objects.all():
    print(user.username)
    print(user.last_login)