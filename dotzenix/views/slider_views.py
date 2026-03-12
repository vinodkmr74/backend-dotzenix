from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Slider
from ..serializers import SliderSerializer
# from rest_framework.parsers import MultiPartParser, FormParser


class SliderAPIView(APIView):

    def get(self, request ,pk=None):
        id=pk
        if id is not None:
           slider = Slider.objects.get(id=pk)
           serializer = SliderSerializer(slider)
           return Response(serializer.data)
    
        
        sliders = Slider.objects.all()
        serializer = SliderSerializer(sliders, many=True)
        return Response(serializer.data)
  
 

    def post(self, request):
        serializer = SliderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"massege":"created succssefully","data": serializer.data})
        return Response(serializer.errors)
    
    def patch(self , request, pk):
        # parser_classes = [MultiPartParser, FormParser]

        id=pk
        slider = Slider.objects.get(id=id)
        serializer = SliderSerializer(slider, data = request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"massege":"updated succssefully","data": serializer.data})
        return Response(serializer.errors)
    
    def delete(self, request, pk):
        slider = Slider.objects.get(id=pk)
        slider.delete()
        return Response({"massege":"Delete successfully"})