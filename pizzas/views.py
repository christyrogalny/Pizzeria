from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, 'pizzas/index.html')


def pizza(request):
    pizza = Pizza.objects.all()

    context = {'all_pizza':pizza}

    return render(request, 'pizzas/pizza.html', context)

def pizzas(request, pizza_id):
    p = Pizza.objects.get(id=pizza_id)

    toppings = Topping.objects.filter(pizza=p)

    context = {'pizzas':p,'toppings':toppings}

    return render(request, 'pizzas/pizzas.html', context)


def addcomment(request, pizza_id):
    if request.method == 'POST' and request.POST.get("btn1"):
        comment = request.POST.get("comment") 
        Comment.objects.create(post_id=pizza_id, text=comment)

    comments = Comment.objects.filter(post=pizza_id)
    post = Pizza.objects.get(id=pizza_id)

    context = {'post':post, 'comments':comments}
    return render(request, 'pizzas/addcomment.html', context)