from django.core.serializers import serialize
from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from openshop.serializers import ProductSerializer
from .models import Product

# Create your views here.
class Productlist(APIView):
    def post(self, request):
        products = ProductSerializer(data=request.data, context={'request': request})
        if products.is_valid():
            products.save()
            return Response(products.data, status=status.HTTP_201_CREATED)

        return Response(products.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response({
            "products": serializer.data,
        }, status=status.HTTP_200_OK)

class ProductDetail(APIView):
    def get_product_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        product = self.get_product_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


    def put(self, request, pk):
        product = self.get_product_object(pk)
        serializer = ProductSerializer(product, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_product_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)