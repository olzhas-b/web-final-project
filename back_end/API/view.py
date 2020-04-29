from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from API.models import Feedback
from API.serializers import FeedBackSerializer



