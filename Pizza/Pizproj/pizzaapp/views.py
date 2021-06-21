from django.shortcuts import render,HttpResponse,get_object_or_404
from rest_framework.decorators import APIView
from django.http import Http404
from django.http import JsonResponse
from rest_framework.response import Response
from .serializers import PizzaSerializer,TypeSerializer,SizeSerializer,ToppingSerializer
from rest_framework import status
from .models import Pizza,Topping,Type,Size
# Create your views here.
class Overview (APIView):
    def get(self,request):
        info={
            'create-pizza':'create a pizza with suitable details',
            'list-pizza-0':'To list all pizza\'s',
            'list-pizza?<i>=<val>':'Here <val> represent that , on what basis pizza should be listed (size,type,topping,) and i for id',
        }
        return Response(info)
class CreatePizza(APIView):
    #Here should be the post request to create new pizza
    def get(self,request):
        data={
        "name": "<pizzaname>",
        "toppings": [
            {
                "name": "toppingname1"
            },
            {
                "name": "toppingname2"
            }
        ],
        "sizes": [
            {
                "val": "large"
            },
            {
                "val": "Small"
            }
        ],
        "types": [
            {
                "name": "Square or Regular (Only one is allowed)"
            }
        ]
        }
        return Response(data,status=status.HTTP_200_OK)
    def post(self,request,format=None):
        serializer=PizzaSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ListPizza(APIView):
    def get(self,request,i):
        pizaobject=Pizza.objects.all()
        serializer=PizzaSerializer(pizaobject,many=True)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    #here should be get and update api to update the pizza.
    def put(self,request,i):
        if(i!=0):
            val=get_object_or_404(Pizza,id=i)
            if('name' not in request.data):
                request.data['name']=''
            if('toppings' not in request.data):
                request.data['toppings']=[]
            if('sizes' not in request.data):
                request.data['sizes']=[]
            if('types' not in request.data):
                request.data['types']=[]
            serializer=PizzaSerializer(instance=val,data=request.data)
            if(serializer.is_valid()):
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,i):
        if(i!=0):
            obj=v=get_object_or_404(Pizza,name=i)
            obj.delete()
        pizaobject=Pizza.objects.all()
        serializer=PizzaSerializer(pizaobject,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
class SpecificList(APIView):
    def get(self,request,i,val):
        if(i=='type'):
            v=get_object_or_404(Type,name=val)
            serializer=PizzaSerializer(v.pizzas.all(),many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        elif(i=='size'):
            v=get_object_or_404(Size,val=val)
            serializer=PizzaSerializer(v.pizzas.all(),many=True)
            return Response(serializer.data,status=status.HTTP_200_OK) 
        elif(i=='topping'):
            v=get_object_or_404(Topping,name=val)
            serializer=PizzaSerializer(v.pizzas.all(),many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)