from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import ProductCard
from ..serializers import ProductCardSerializer 



class ProductCardViewSet(APIView):
    def get(self, request, pk=None):
        id=pk
        if id is not None:
            productcard = ProductCard.objects.get(id=pk)
            serializer = ProductCardSerializer(productcard)
            return Response(serializer.data)


        productcard = ProductCard.objects.all()
        serializer = ProductCardSerializer(productcard, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductCardSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"massege":"created succssefully","data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request,pk):
        productcard = ProductCard.objects.get(id=pk)
        serializer = ProductCardSerializer(productcard, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"massege":"updated succssefully","data": serializer.data})
        return Response(serializer.errors)
    def put(self, request,pk):
        productcard = ProductCard.objects.get(id=pk)
        serializer = ProductCardSerializer(productcard,data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"massege":"updated succssefully","data": serializer.data})
        return Response(serializer.errors)
      
    def delete(self, request,pk):
        productcard = ProductCard.objects.get(id=pk)
        productcard.delete()
        return Response({"massege":"deleted succssefully"})