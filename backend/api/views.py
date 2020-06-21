from rest_framework import mixins, viewsets
from rest_framework.response import Response
from .serializer import *
from database.models import *
# Create your views here.

class MSTProductViewSet(viewsets.ModelViewSet):
    queryset = MSTProduct.objects.all()
    serializer_class = MSTProductSerializer

    def sorter(self,data):
        max_seats = abs(data["max_seats"] - 2)
        dimension_list = [int(n) for n in data["dimension"].split(" x ")]
        result = 1
        for number in dimension_list:
            result *= number
        dimension = abs(result - (162*95*86))
        colors = not set([detail["color"] for detail in data["details"]]) == set(["custard vienna", "graphite vienna", "ruby vienna"])
        price = abs(data["price"]-3899000)
        material = not data["material"] == "solid wood"
        return(max_seats, dimension, material, colors, price)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = MSTProductSerializer(queryset,many=True)
        serializer_data = sorted(serializer.data, key=self.sorter)
        return Response(serializer_data)

class TRXProductViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    queryset = TRXProduct.objects.all()
    serializer_class = TRXProductSerializer

