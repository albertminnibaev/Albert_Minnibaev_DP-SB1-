from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from .filters import AdFilter
from .models import Ad, Comment
from .permissions import IsAuthor, IsAdmin, IsAnonymous
from .serializers import AdSerializer, AdDetailSerializer, CommentSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    pagination_class = AdPagination
    filter_backends = (DjangoFilterBackend,)  # Подключаем библотеку, отвечающую за фильтрацию к CBV
    filterset_class = AdFilter  # Выбираем наш фильтр

    def get_serializer_class(self):
        if self.action in ['retrieve', 'create', 'update', 'partial_update']:
            return AdDetailSerializer
        return AdSerializer

    def list(self, request, *args, **kwargs):
        queryset = Ad.objects.all()

        # данный код необходим для того чтобы работала пагинация
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = AdSerializer(queryset, many=True)
        return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     queryset = Ad.objects.all()
    #     course = get_object_or_404(queryset, pk=pk)
    #     serializer = AdDetailSerializer(course)
    #     return Response(serializer.data)

    def perform_create(self, serializer):
        new_ad = serializer.save()
        new_ad.author = self.request.user
        new_ad.save()

    def get_permissions(self):
        if self.action in ['create']:
            return [IsAuthenticated()]
        if self.action in ['list']:
            return [(IsAuthenticated | IsAnonymous)()]
        # if self.action in ['destroy', 'retrieve', 'update']:
        #     return [(IsAuthor | IsAdmin)()]
        return [(IsAuthor | IsAdmin)()]

    @action(detail=False)
    def me(self, request, *args, **kwargs):
        self.queryset = Ad.objects.filter(author=request.user)
        return super().list(self, request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    pagination_class = AdPagination

    def list(self, request, *args, **kwargs):
        ad_id = self.kwargs.get('ad_pk')
        queryset = Comment.objects.filter(ad_id=ad_id)

        # данный код необходим для того чтобы работала пагинация
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        new_comment = serializer.save()
        ad_id = self.kwargs.get('ad_pk')
        new_comment.author = self.request.user
        new_comment.ad = get_object_or_404(Ad, pk=ad_id)
        new_comment.save()

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [(IsAuthor | IsAdmin)()]
        return [IsAuthenticated()]
