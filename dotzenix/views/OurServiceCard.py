from rest_framework.response import Response
from rest_framework import status
from ..models import OurServiceCard
from ..serializers import OurServiceCardSerializer
from rest_framework.views import APIView


class OurServiceCardViewSet(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            ourservicecard = OurServiceCard.objects.get(id=pk)
            serializers = OurServiceCardSerializer(ourservicecard)
            return Response(serializers.data)

        ourservicecard = OurServiceCard.objects.all()
        serializers = OurServiceCardSerializer(ourservicecard, many=True)
        return Response(serializers.data)
    
    def post(self, request):
        serializer = OurServiceCardSerializer(data=request.data , many=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"massege":"created succssefully","data":serializer.data}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        id=pk
        ourservicecard = OurServiceCard.objects.get(id=id)
        serializer = OurServiceCardSerializer(ourservicecard, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Updated successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        id=pk
        ourservicecard = OurServiceCard.objects.get(id=id)
        serializer = OurServiceCardSerializer(ourservicecard, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Updated successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request, pk):
        ourservicecard = OurServiceCard.objects.get(pk=pk)
        ourservicecard.delete()
        return Response({"massege":"Delete successfully"})