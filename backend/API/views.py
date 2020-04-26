from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from API.models import Company, Vacancy
from django.views.decorators.csrf import csrf_exempt
from API.serializers import ProductSerializer, UserSerializer
import json
# Create your views here
@csrf_exempt
def list_products(request):
    if request.method == 'GET':
        data = Product.objects.all()
        serializer = ProductSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        request_body = json.loads(request.body)
        serializer = ProductSerializer(data=request_body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.error)
    return JsonResponse({"bad request"})

@csrf_exempt
def getProductById(request, id):
    try:
        product = Product.objects.get(id=id)
    except:
        return HttpResponse("Error not found " + str(id))
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        request_body = json.loads(request.body)
        serializer = ProductSerializer(instance=product, data=request_body)
        if serializer.is_valid():
            serializer.save()
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'DELETE':
        product.delete()

@csrf_exempt
def getUserById(request, id):
    try:
        user = User.objects.get(id=id)
    except:
        return HttpResponse("Error not found " + str(id))
    try:
        user_data = user.vacancy_set.all()
        user_json = [i.to_json() for i in user_data]
        return JsonResponse(vacancy_json, safe=False)
    except:
        return HttpResponse('error')

def list_comment(request):
    comments = Comment.objects.all()
    comment_json = [comment.to_json() for comment in comments]
    return JsonResponse(comment_json, safe=False)

def getCommentByIdById(request, id):
    try:
        comment = Comment.objects.get(id=id)
        return JsonResponse(comment.to_json(), safe=False)
    except:
        return HttpResponse(str(id) + " didn't find")

def getTopTen(request):
    try:
        product = Product.objects.order_by("-price")
        product = [i.to_json() for i in product[:5]]
        return JsonResponse(product, safe=False)
    except:
        return HttpResponse(str(id) + " didn't find")
