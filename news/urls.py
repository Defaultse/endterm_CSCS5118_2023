from django.urls import path
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from .views.news import *
from .views.auth import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'moderators', ModeratorViewSet, basename='moderators')
router.register(r'news', NewsViewSet, basename='news')


urlpatterns = [    
    path('news/', ListNewsView.as_view(), name='list_news'), #gets all news, without auth

    path('auth/', ModeratorTokenObtainView.as_view(), name='token_obtain_pair'), #auth token for moderators

    path('news/create', CreateNewsView.as_view(), name='create_news'), #creating news, needs authentification. Only by moderators
    path('news/by-token/', NewsByTokenView.as_view(), name='news_by_token'), #get all news of moderator by his token
    path('news/<int:pk>/update/', UpdateNewsView.as_view(), name='update_news'),  #update news by id
]
