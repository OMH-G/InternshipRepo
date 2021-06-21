from rest_framework import serializers
from . models import Pizza,Topping,Size,Type

class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Topping    
        fields=('name',)
class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Size    
        fields=('val',)
class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Type    
        fields=('name',)
class PizzaSerializer(serializers.ModelSerializer):
    toppings=ToppingSerializer(many=True)
    sizes=SizeSerializer(many=True)
    types=TypeSerializer(many=True)
    class Meta:
        model=Pizza
        fields=('id','name','toppings','sizes','types')
    def create(self, validated_data):
        temp_topping = validated_data.pop('toppings')
        temp_size = validated_data.pop('sizes')
        temp_types = validated_data.pop('types')
        topping,size,types=[],[],[]
        for i in temp_topping:
            if(i in topping):continue
            topping.append(i)
        for i in temp_size:
            if(i in size):continue
            size.append(i)
        for i in temp_types:
            if(i in types):continue
            types.append(i)
        piza = Pizza.objects.create(**validated_data)
        for i in topping:
            val=dict(i)
            try:
                v=Topping.objects.get(name=val['name'])
                piza.toppings.add(v)
            except:
                piza.toppings.add(Topping.objects.create(**val))
        for i in size:
            val=dict(i)
            try:
                v=Size.objects.get(val=val['val'])
                piza.sizes.add(v)
            except:
                one=Size.objects.create(**val)
                piza.sizes.add(one)
        for i in types:
            val=dict(i)
            try:
                v=Type.objects.get(name=val['name'])
                piza.types.add(v)
            except:
                piza.types.add(Type.objects.create(**val))
        return piza
    def update(self, instance, validated_data):
        if(validated_data['name']!=''):
            instance.name=validated_data.get('name',instance)
        if(validated_data['toppings']!=[]):
            for i in validated_data.get('toppings',instance.toppings):
                try:
                    if(instance.toppings.get(name=f"{i['name']}")):
                        continue
                except:
                    store=Topping.objects.create(**dict(i))
                    instance.toppings.add(store)
        if(validated_data['sizes']!=[]):
            for i in validated_data.get('sizes',instance.sizes):

                try:
                    if(instance.sizes.get(val=f"{i['val']}")):
                        continue
                except:
                    store=Size.objects.create(**dict(i))
                    instance.sizes.add(store)
        if(validated_data['types']!=[]):
            val=dict(validated_data.get('types')[0])
            if(len(instance.types.all())!=0):
                instance.types.all()[0].delete()
            if(val['name']=='Square'):
                store=Type.objects.create(name='Square')
                instance.types.add(store)
            elif(val['name']=='Regular'):
                store=Type.objects.create(name='Regular')
                instance.types.add(store)
        instance.save()
        return instance