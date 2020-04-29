from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from API.models import Products, Category, Feedback
from django.http import JsonResponse, HttpResponse
from API.serializers import CategorySerializer, ProductsSerializer, FeedBackSerializer
from django.views.decorators.csrf import csrf_exempt
import json


# @csrf_exempt
# class FeedBackList(generics.ListCreateAPIView):
#     queryset = Feedback.objects.all()
#     serializer_class = FeedBackSerializer
#     permission_classes = (IsAuthenticated,)



@csrf_exempt
def list_products(request):
    if request.method == 'GET':
        data = Products.objects.all()
        serializer = ProductsSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        request_body = json.loads(request.body)
        serializer = ProductsSerializer(data=request_body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.error)
    return JsonResponse({"bad request"})

@csrf_exempt
def list_categories(request):
    if request.method == 'GET':
        data = Category.objects.all()
        serializer = CategorySerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        request_body = json.loads(request.body)
        serializer = CategorySerializer(data=request_body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.error)

@csrf_exempt
def getProductById(request, id):
    if request.method == 'GET':
        data = Products.objects.get(id=id)
        serializer = ProductsSerializer(data, many=False)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        request_body = json.loads(request.body)
        product = Products.objects.get(id=id)
        serializer = ProductsSerializer(instance=product, data=request_body)
        if serializer.is_valid():
            serializer.save()
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'DELETE':
        product = Products.objects.get(id=id)
        product.delete()

@csrf_exempt
def list_feedback(request):
    if request.method == 'GET':
        data = Feedback.objects.all()
        serializer = FeedBackSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        request_body = json.loads(request.body)
        serializer = FeedBackSerializer(data=request_body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.error)

def deleteCategoryById(request, id):
    if request.method == 'DELETE':
        category = Category.objects.get(id=id)
        category.delete()
