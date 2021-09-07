from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


from django.shortcuts import render, redirect

from product.api.serializers import ProductSerializer
from product.models import Product


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def cart(request, pk):
    if request.method == 'GET':
        response = dict()
        response['products'] = ProductSerializer(Product.objects.filter(id=pk), many=True).data

        request.session['products'] = response
        print(request.session['products'])

    return redirect('product:index')

