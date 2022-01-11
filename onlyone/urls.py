from django.db.models import base
from django.urls import path, include
from rest_framework import routers
from .views import ChatViewSet, ClientViewSet, FriendViewSet, KeydatumViewSet, SearchFriendViewSet, OfferViewSet
router = routers.DefaultRouter()
router.register('clients', ClientViewSet)
router.register('chat', ChatViewSet, basename="chating")
router.register('friends', FriendViewSet, basename='friends_basename')
router.register('keydatum', KeydatumViewSet)
router.register('searchfriend', SearchFriendViewSet, basename='igrek')
router.register('offers', OfferViewSet, basename='offers_basename')
urlpatterns = [
    path('', include(router.urls))
]