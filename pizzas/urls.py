from django.urls import path
from . import views 


app_name = 'pizzas'

urlpatterns = [ 
    path('',views.index,name='index'),
    path('pizza',views.pizza,name='pizza'),
    path('pizza/<int:pizza_id>/',views.pizzas,name='pizzas'),
    path('pizza/<int:pizza_id>/addcomment', views.addcomment, name='addcomment'),
]
