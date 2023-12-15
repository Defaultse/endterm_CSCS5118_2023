from rest_framework import generics, status, viewsets, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from news.models import Moderator, News
from news.permissions import IsNewsOwnerPermission
from news.serializers import *

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class CreateNewsView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CreateNewsSerializer

    def perform_create(self, serializer):
        serializer.save(moderator=self.request.user)

class ListNewsView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class NewsByTokenView(generics.ListAPIView):
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        moderator = self.request.user
        queryset = News.objects.filter(moderator=moderator)
        return queryset
    
class UpdateNewsView(generics.UpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsUpdateSerializer 
    permission_classes = [permissions.IsAuthenticated, IsNewsOwnerPermission]

