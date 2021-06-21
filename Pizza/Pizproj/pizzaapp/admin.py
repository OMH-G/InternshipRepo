from django.contrib import admin
from . models import Topping,Type,Size,Pizza
# Register your models here.
admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Type)
admin.site.register(Size)