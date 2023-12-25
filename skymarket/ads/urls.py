from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter

from .apps import SalesConfig
from .views import AdViewSet, CommentViewSet


app_name = SalesConfig.name

ads_router = DefaultRouter()
ads_router.register(r'ads', AdViewSet, basename='ads')
comments_router = NestedSimpleRouter(ads_router, r'ads', lookup='ad')
comments_router.register("comments", CommentViewSet, basename='ads')

urlpatterns = [
    path('', include(ads_router.urls)),
    path('', include(comments_router.urls)),
]
