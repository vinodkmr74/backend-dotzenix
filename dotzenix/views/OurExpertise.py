from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import OurExpertise
from ..serializers import OurExpertiseSerializer
from rest_framework import status



class OurExpertiseViewSet(APIView):
    
    def get(self,request,pk=None):
        id=pk
        if id is not None:
            ourexpertise = OurExpertise.objects.get(id=pk)
            serializer = OurExpertiseSerializer(ourexpertise)
            return Response(serializer.data)
            
        ourexpertise = OurExpertise.objects.all()
        serializer = OurExpertiseSerializer(ourexpertise,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = OurExpertiseSerializer(data=request.data ,many=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"massege":"created succssefully","data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            
    def put(self, request, pk=None):
      id=pk
      ourexpertise = OurExpertise.objects.get(id=id)
      serializer = OurExpertiseSerializer(ourexpertise, data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response({"massege":"updated succssefully","data": serializer.data})
      return Response(serializer.errors)
     
    def patch(self, request, pk=None):
      id=pk
      ourexpertise = OurExpertise.objects.get(id=id)
      serializer = OurExpertiseSerializer(ourexpertise, data=request.data, partial=True)
      if serializer.is_valid():
          serializer.save()
          return Response({"massege":"updated succssefully","data": serializer.data})
      return Response(serializer.errors)
  
    def delete(self, request, pk=None):
      id=pk
      ourexpertise = OurExpertise.objects.get(id=id)
      ourexpertise.delete()
      return Response({"massege":"deleted succssefully"})
  
  
        