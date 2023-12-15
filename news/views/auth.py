from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status, viewsets, generics
from news.serializers import *
from news.models import Moderator

class ModeratorViewSet(viewsets.ModelViewSet):
    queryset = Moderator.objects.all()
    serializer_class = ModeratorSerializer

class ModeratorTokenObtainView(TokenObtainPairView):
    serializer_class = ModeratorTokenObtainSerializer

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)

# class ModeratorTokenObtainPairView(TokenObtainPairView):
#     serializer_class = ModeratorTokenObtainPairSerializer
