from django.db import models

# Create your models here.
class Topping(models.Model):
    name=models.CharField(max_length=50,null=False,default='')
    def __str__(self):
        return self.name
class Type(models.Model):
    piza_type=[
        ('Regular','Regular'),('Square','Square')
    ]
    name=models.CharField(max_length=50,choices=piza_type,default='')
    def __str__(self):
        return self.name 
class Size(models.Model):
    sizes_of_pizza=[
        ('Small','Small'),
        ('Medium','Medium'),
        ('Large','Large'),
        ('Extra-Large','Extra-Large')
    ]
    val=models.CharField(max_length=50,default='Small',choices=sizes_of_pizza)
    def __str__(self):
        return self.val
class Pizza(models.Model):
    name=models.CharField(max_length=50,null=True,default='')
    toppings=models.ManyToManyField('Topping', related_name='pizzas')
    sizes=models.ManyToManyField('Size', related_name='pizzas')
    types=models.ManyToManyField('Type', related_name='pizzas')
    def __str__(self):
        return self.name

