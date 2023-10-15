from app.models import Product
from django.shortcuts import render
from django.http import JsonResponse
from .products import products
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ProductSerializer 

# Create your views here.


@api_view(['GET'])
def getRoutes(request):
    return Response('Hello')



@api_view(['GET'])
def getProducts(request):
    products=Product.objects.all()
    serializer=ProductSerializer(products,many=True)
    return Response(serializer.data)







@api_view(['GET'])
def getProducts(request):
    return Response(products)


@api_view(['GET'])
def getProduct(request, pk):
    product = None
    for i in products:
        if i['_id'] == pk:
            product = i
            break
    if product:
        return Response(product)
    else:
        return Response({'detail': 'Product not found'})
