from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import OurServiceSubitemCard
from ..serializers import OurServiceSubitemCardSerializer

class SubitemUpdateView(APIView):
    
    def get(self, request, pk=None):
        
        if pk is None:
            subitem = OurServiceSubitemCard.objects.all()
            serializer = OurServiceSubitemCardSerializer(subitem, many=True)
            return Response(serializer.data)
        
        subitem = OurServiceSubitemCard.objects.get(id=pk)
        serializer = OurServiceSubitemCardSerializer(subitem)
        return Response(serializer.data)

    def patch(self, request, pk):
        subitem = OurServiceSubitemCard.objects.get(id=pk)

        serializer = OurServiceSubitemCardSerializer(
            subitem,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)