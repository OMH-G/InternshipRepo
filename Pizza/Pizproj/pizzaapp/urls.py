from django.urls import path
from .views import Overview,CreatePizza,ListPizza,SpecificList
urlpatterns = [
    path('',Overview.as_view(), name="overview"),
    path('create-pizza/',CreatePizza.as_view(), name="CreatePizza"),
    path('list-pizza=<int:i>',ListPizza.as_view(), name="ListPizza"),
    path('list-pizza-<str:i>=<str:val>',SpecificList.as_view(), name="ListPizza"),
]
 