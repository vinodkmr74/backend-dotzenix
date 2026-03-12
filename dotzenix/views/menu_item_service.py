from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ..models import MenuItemServices
from ..serializers import MenuItemServiceSerializer
class MenuItemServiceViewSet(APIView):
    def get(self, request ,pk=None):
        id=pk
        if id is not None:
           service = MenuItemServices.objects.get(id=pk)
           serializer = MenuItemServiceSerializer(service)
           return Response(serializer.data)

        menu_item_services = MenuItemServices.objects.all()
        serializer = MenuItemServiceSerializer(menu_item_services, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MenuItemServiceSerializer(data=request.data , many=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"massege":"created succssefully","data":serializer.data}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, pk):
        id=pk
        menu = MenuItemServices.objects.get(id=id)
        serializer = MenuItemServiceSerializer(menu, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Updated successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        id=pk
        menu = MenuItemServices.objects.get(id=id)
        serializer = MenuItemServiceSerializer(menu, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Updated successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        menu = MenuItemServices.objects.get(id=pk)
        menu.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"massege":"Delete successfully"})