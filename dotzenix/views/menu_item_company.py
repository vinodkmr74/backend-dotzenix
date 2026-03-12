from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import MenuItemCompany
from ..serializers import MenuItemSerializer


class MenuAPIView(APIView):

    def get(self, request ,pk=None):
        id=pk
        if id is not None:
            menu = MenuItemCompany.objects.get(id=pk)
            serializer = MenuItemSerializer(menu, many=False)
            return Response(serializer.data)
        
        menu = MenuItemCompany.objects.all()
        serializer = MenuItemSerializer(menu, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MenuItemSerializer(data=request.data , many=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"massege":"created succssefully","data":serializer.data}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        id=pk
        menu = MenuItemCompany.objects.get(id=id)
        serializer = MenuItemSerializer(menu, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
    "message": "Updated successfully",
    "data": serializer.data
}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        id=pk
        menu = MenuItemCompany.objects.get(id=id)
        serializer = MenuItemSerializer(menu, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({
    "message": "Updated successfully",
    "data": serializer.data
  }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        menu = MenuItemCompany.objects.get(id=pk)
        menu.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"massege":"Delete successfully"})
