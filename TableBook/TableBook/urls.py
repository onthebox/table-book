from django.contrib import admin
from django.urls import include, path

from user_service.views import ChainViewSet, BranchViewSet
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('chain', ChainViewSet)
router.register('branch', BranchViewSet)


urlpatterns = [
    path('', include(router.urls)),

]