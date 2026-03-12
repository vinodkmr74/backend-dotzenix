from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import ContactBar
from ..serializers import ContactBarSerializer


@api_view(['POST'])
def create_contact(request):
    serializer= ContactBarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "data": serializer.data,
            "massege": "succssfully"},status=201)
    return Response({
        "data": serializer.errors,
        "massege": "filds contact data"
        }, status=400)

@api_view(['GET'])
def get_contact(request):
    contact=ContactBar.objects.all()
    serializer= ContactBarSerializer(contact, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_contact_id(request, pk):
    contact=ContactBar.objects.get(id=pk)
    serializer= ContactBarSerializer(contact, many=False)
    return Response(serializer.data)
@api_view(['PUT'])
def update_contact(request, pk):
    contact=ContactBar.objects.get(id=pk)
    serializer= ContactBarSerializer(instance=contact, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "data": serializer.data,
            "massege": "updated succssfully"},status=201)
    return Response({
        "data": serializer.errors,
        "massege": "filds contact data"
        }, status=400)
    
@api_view(['DELETE'])
def delete_contact(request, pk):
    contact=ContactBar.objects.get(id=pk)
    contact.delete()
    return Response({"message": "Deleted successfully"})