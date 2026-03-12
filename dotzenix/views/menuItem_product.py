from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ..models import MenuItemProducts
from ..serializers import MenuItemProjectSerializer

class ProductsViewSet(APIView):
    def get(self, request ,pk=None):
        id=pk
        if id is not None:
           product = MenuItemProducts.objects.get(id=pk)
           serializer = MenuItemProjectSerializer(product)
           return Response(serializer.data)

        menu_item_products = MenuItemProducts.objects.all()
        serializer = MenuItemProjectSerializer(menu_item_products, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MenuItemProjectSerializer(data=request.data , many=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"massege":"created succssefully","data":serializer.data}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):  
        id=pk    
        menu = MenuItemProducts.objects.get(id=id)
        serializer = MenuItemProjectSerializer(menu, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Updated successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, pk):
        id=pk
        menu = MenuItemProducts.objects.get(id=id)
        serializer = MenuItemProjectSerializer(menu, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Updated successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        menu = MenuItemProducts.objects.get(id=pk)
        menu.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"massege":"Delete successfully"})