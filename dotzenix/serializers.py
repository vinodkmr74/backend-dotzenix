from rest_framework import serializers
from .models import ContactBar, MenuItemCompany, Slider, MenuItemServices,MenuItemProducts
from .models import  MenuItemServiceItems


class ContactBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactBar
        fields = "__all__"

    def validate_mob(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Mobile must contain only digits")

        if len(value) != 10:
            raise serializers.ValidationError("Mobile number must be 10 digits")

        return value

#  ..............MenuItemCompany..............
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItemCompany
        fields = "__all__"
# ..............MenuItemServices..............


class MenuItemServiceItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItemServiceItems
        fields = ["name", "path"]
class MenuItemServiceSerializer(serializers.ModelSerializer):
    items = MenuItemServiceItemsSerializer(many=True)

    class Meta:
        model = MenuItemServices
        fields = ["id","title", "items"] 
        
    def create(self, validated_data):
        items_data = validated_data.pop("items",[]) 
        service = MenuItemServices.objects.create(**validated_data)
        for item in items_data:
            MenuItemServiceItems.objects.create(service=service, **item)
        return service  
    
    # ...................prodect...............
class MenuItemProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItemProducts
        fields = "__all__"
           
# ................ slider...............
class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = "__all__"