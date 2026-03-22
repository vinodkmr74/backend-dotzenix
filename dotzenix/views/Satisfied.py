from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from ..models import Satisfied
from ..serializers import SatisfiedSerializer



class SatisfiedViewSet(APIView):
    def get(self, request, pk=None):
       id=pk
       
       if id is not None:
           satisfied = Satisfied.objects.get(id=pk)
           serializer = SatisfiedSerializer(satisfied)
           return Response(serializer.data)

       satisfied = Satisfied.objects.all()
       serializer = SatisfiedSerializer(satisfied, many=True)
       return Response(serializer.data)
   
    def post(self, request):
      serializer = SatisfiedSerializer(data=request.data, many=True)
      if serializer.is_valid():
          serializer.save()
          return Response({"massege":"created succssefully","data": serializer.data}, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    def put(self, request, pk=None):
      id=pk
      satisfied = Satisfied.objects.get(id=id)
      serializer = SatisfiedSerializer(satisfied, data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response({"massege":"updated succssefully","data": serializer.data})
      return Response(serializer.errors)
     
    def patch(self, request, pk=None):
      id=pk
      satisfied = Satisfied.objects.get(id=id)
      serializer = SatisfiedSerializer(satisfied, data=request.data, partial=True)
      if serializer.is_valid():
          serializer.save()
          return Response({"massege":"updated succssefully","data": serializer.data})
      return Response(serializer.errors)
  
    def delete(self, request, pk=None):
      id=pk
      satisfied = Satisfied.objects.get(id=id)
      satisfied.delete()
      return Response({"massege":"deleted succssefully"})
  
  