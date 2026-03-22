from rest_framework.views import APIView
from ..serializers import MissionVisionSerializer
from ..models import MissionVission  
from rest_framework.response import Response
from rest_framework import status


class MissionVisionView(APIView):
    def get(self, request, pk=None):
        
        id=pk
        if id is not None:
            missionvission = MissionVission.objects.get(id=pk)
            serializer = MissionVisionSerializer(missionvission)
            return Response(serializer.data)
     
        missionvission = MissionVission.objects.all()
        serializer = MissionVisionSerializer(missionvission, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MissionVisionSerializer(data=request.data , many=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None):
        id=pk
        missionvission = MissionVission.objects.get(id=id)
        serializer = MissionVisionSerializer(missionvission, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk=None):
        id=pk
        missionvission = MissionVission.objects.get(id=id)
        serializer = MissionVisionSerializer(missionvission, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None):
        id=pk
        missionvission = MissionVission.objects.get(id=id)
        missionvission.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
