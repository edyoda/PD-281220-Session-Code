from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse, HttpResponse
from django.views.generic.base import View
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, GenericViewSet
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination

from .models import Article
from .serializers import ArticleSerializer


class MyPagination(PageNumberPagination):
    page_size = 6
    page_size_query_param = "page_size"
    max_page_size = 20


class ArticleGenericViewSet(GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, 
mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):

    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    pagination_class = MyPagination

    def get_queryset(self): # Generic View Sets and Generic Views
        qs = super().get_queryset()
        author = self.request.query_params.get("author", None)
        if author:
            qs = qs.filter(author = author)
        return qs


# Viewset are specifically designed for CRUD Operations
# list fetch
# create - creating
class ArticleViewSet(ViewSet, PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 20


    # Get all Data
    def list(self, request):
        articles = Article.objects.all()
        author = request.query_params.get("author", None)
        if author:
            articles = articles.filter(author = author)
        result_set = self.paginate_queryset(articles, request, view=self)
        serializers = ArticleSerializer(result_set, many=True)
        # return Response(serializers.data)
        return self.get_paginated_response(serializers.data)

    # Post a given data
    def create(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Get Specifc data
    def retrieve(self, request, pk):
        qs = Article.objects.all()
        article = get_object_or_404(qs, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    # PUT
    def update(self, request, pk):
        qs = Article.objects.all()
        article = get_object_or_404(qs, pk=pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete
    def destroy(self, request, pk):
        qs = Article.objects.all()
        article = get_object_or_404(qs, pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ArticleListView(APIView, MyPagination):

    def get(self, request):
        articles = Article.objects.all()
        author = request.query_params.get("author", None)
        if author:
            articles = articles.filter(author = author)
        result_set = self.paginate_queryset(articles, request, view=self)
        serializers = ArticleSerializer(result_set, many=True)
        # return Response(serializers.data)
        return self.get_paginated_response(serializers.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailView(APIView):
    def get_article(self, id):
        try:
            return Article.objects.get(id=id)
        except:
            return None

    def get(self, request, pk):
        article = self.get_article(pk)
        if article:
            serializer = ArticleSerializer(article)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        article = self.get_article(pk)
        if article:
            serializer = ArticleSerializer(article, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        article = self.get_article(pk)
        if article:
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)

