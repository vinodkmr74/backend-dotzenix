from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import HeddingSunhedding
from ..serializers import HeddingSunheddingSerializer


class HeddingSunheddingAPIView(APIView):
    def get(self, request, pk = None):
        if pk is not None:
           hedding = HeddingSunhedding.objects.get(id=pk)
           serializer = HeddingSunheddingSerializer(hedding)
           return Response(serializer.data)

        hedding = HeddingSunhedding.objects.all()
        serializer = HeddingSunheddingSerializer(hedding, many=True)
        return Response(serializer.data)  
    
    
    def post(self, request):
        serializer = HeddingSunheddingSerializer(data=request.data)
        
        if serializer.is_valid():
        
            serializer.save()
            return Response({"massege":"created succssefully","data": serializer.data})
        
    def patch(self , request, pk):
        # parser_classes = [MultiPartParser, FormParser]

        id=pk
        hedding = HeddingSunhedding.objects.get(id=id)
        serializer = HeddingSunheddingSerializer(hedding, data = request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"massege":"updated succssefully","data": serializer.data})
        return Response(serializer.errors)
    
    def delete(self, request, pk):
        hedding = HeddingSunhedding.objects.get(id=pk)
        hedding.delete()
        return Response({"massege":"Delete successfully"})  