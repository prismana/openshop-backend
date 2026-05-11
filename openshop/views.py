from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from openshop.serializers import ProductSerializer

# Create your views here.
class Productlist(APIView):
    def post(self, request):
        products = ProductSerializer(data=request.data, context={'request': request})
        if products.is_valid():
            products.save()
            return Response(products.data, status=status.HTTP_201_CREATED)

        return Response(products.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        return Response('hello', status=status.HTTP_200_OK)