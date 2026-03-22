from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import ExploreOur
from ..serializers import ExploreOurSerializer
from rest_framework import status



class ExploreOurViewSet(APIView):
    
    def get(self,request,pk=None):
        id=pk
        if id is not None:
            exploreour = ExploreOur.objects.get(id=pk)
            serializer = ExploreOurSerializer(exploreour)
            return Response(serializer.data)
            
        exploreour = ExploreOur.objects.all()
        serializer = ExploreOurSerializer(exploreour,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ExploreOurSerializer(data=request.data ,many=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"massege":"created succssefully","data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            
    def put(self, request, pk=None):
      id=pk
      exploreour = ExploreOur.objects.get(id=id)
      serializer = ExploreOurSerializer(exploreour, data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response({"massege":"updated succssefully","data": serializer.data})
      return Response(serializer.errors)
     
    def patch(self, request, pk=None):
      id=pk
      exploreour = ExploreOur.objects.get(id=id)
      serializer = ExploreOurSerializer(exploreour, data=request.data, partial=True)
      if serializer.is_valid():
          serializer.save()
          return Response({"massege":"updated succssefully","data": serializer.data})
      return Response(serializer.errors)
  
    def delete(self, request, pk=None):
      id=pk
      exploreour = ExploreOur.objects.get(id=id)
      exploreour.delete()
      return Response({"massege":"deleted succssefully"})
  
  
        