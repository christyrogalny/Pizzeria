from django.db import models


# Create your models here.
## model = Pizza
## field = pizza_name (Hawaiian, Meat Lovers, etc.)
class Pizza(models.Model):
    pizza_name = models.CharField(max_length=200)

    def __str__(self):
        return self.pizza_name

## model = Topping
## field 1 = pizza - FK
## field 2 = topping_name (Pineapple, Canadian bacon, sausage, etc.)
class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    pizza_name = models.TextField()

    def __str__(self):
        return self.pizza_name 

## comments 
class Comment(models.Model):
    pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    text = models.TextField(max_length=200)

    def __str__(self):
        return self.text
