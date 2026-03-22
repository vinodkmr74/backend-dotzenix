from rest_framework import serializers
from .models import ContactBar, MenuItemCompany, Slider, MenuItemServices,MenuItemProducts
from .models import  MenuItemServiceItems,HeddingSunhedding,OurServiceSubitemCard,OurServiceCard,ProductCard, MissionVission,Satisfied,OurExpertise,ExploreOur


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
        
        
class HeddingSunheddingSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeddingSunhedding
        fields = "__all__"
        
 # ...................our service card..............
class OurServiceSubitemCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurServiceSubitemCard
        fields = ["id","subitem"]

class OurServiceCardSerializer(serializers.ModelSerializer):
    subitems = OurServiceSubitemCardSerializer(
        many=True,
        read_only=True
        )

    class Meta:
        model = OurServiceCard
        fields = ["id","iconpath","title", "subitems"] 
        
    def create(self,validated_data):
        subitems_data = validated_data.pop("subitems",[]) 
        service = OurServiceCard.objects.create(**validated_data)
        for item in subitems_data:
            OurServiceSubitemCard.objects.create(service=service, **item)
        return service
# .....................product card home..........
class ProductCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCard
        fields = "__all__"
        
#    ............MissionVisioncard.............
class MissionVisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissionVission
        fields = "__all__"

class SatisfiedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Satisfied
        fields = "__all__"
# ..........Our Expertise...........
class OurExpertiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurExpertise
        fields = "__all__"
     # ............Explore Our...........

class ExploreOurSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExploreOur
        fields = "__all__"
