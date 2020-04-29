from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from API.models import Products, Category
from django.views.decorators.csrf import csrf_exempt
from API.serializers import ProductsSerializer, CategorySerializer, FeedBackSerializer

@csrf_exempt
class PostFeedBack(APIView):
    def post(self, request, *args, **kwargs):
        serializer = FeedBackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
