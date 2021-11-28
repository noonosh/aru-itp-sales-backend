from rest_framework.response import Response
from app.models import Car
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework import status
from .serializers import CarSerializer


# Create your views here.


class CarsList(APIView):

    def get(self, request, *args, **kwargs):
        queryset = Car.objects.all()
        serializer = CarSerializer(queryset, many=True)

        return HttpResponse(JSONRenderer().render(serializer.data), content_type='application/json')
