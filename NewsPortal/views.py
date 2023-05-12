from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

from .models import NewsAuthor, NewsCategory, News, NewsTag, NewsComment
from .serializer import AuthorSerializer, CategorySerializer, NewsSerializer, TegSerializer, CommentSerializer, NewsPostSerializer


class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = NewsAuthor.objects.all()


class CategoryViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = NewsCategory.objects.all()

class NewsViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = NewsSerializer
    queryset = News.objects.all()

    # показывает 5 последних новостей
    @action(methods=['get'], detail=False, url_path='get-last-5')
    def get_last_5(self, request):
        queryset = self.queryset.order_by('news_relize_date')[:5]
        data = self.serializer_class(queryset, many=True).data
        return Response(data)

    # фильтрация по категориям
    @action(methods=['get'], detail=False, url_path='filter-category')
    def filter_category(self, request):
        cat = request.query_params.get('category_id')
        queryset = self.get_queryset().filter(category_name=cat)
        data = self.serializer_class(queryset, many=True).data
        return Response(data)

    # просмотр всех новостей сортированных по времени добавления
    @action(methods=['get'], detail=False, url_path='get-news')
    def get_news(self, request):
        queryset = self.queryset.order_by('news_relize_date')
        data = self.serializer_class(queryset, many=True).data
        return Response(data)

    # открывает сериализатор добавления новости
    def get_serializer_class(self):
        if self.action == 'post':
            return NewsSerializer
        return NewsPostSerializer

class CommentViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = CommentSerializer
    queryset = NewsComment.objects.all()

    # филтрация комментариев по id новости
    @action(methods=['get'], detail=False, url_path='filter-comment')
    def filter_comment(self, request):
        news = request.query_params.get('id_news')
        queryset = self.get_queryset().filter(id_news=news)
        data = self.serializer_class(queryset, many=True).data
        return Response(data)

class TegViewSet(ModelViewSet):
    serializer_class = TegSerializer
    queryset = NewsTag.objects.all()
