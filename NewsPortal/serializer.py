from rest_framework.serializers import ModelSerializer
from NewsPortal.models import NewsAuthor, NewsCategory, News, NewsComment, NewsTag


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = NewsAuthor
        fields = ('last_name','first_name','mid_name')


class CategorySerializer(ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = ('name','description')


class CommentSerializer(ModelSerializer):
    class Meta:
        model = NewsComment
        fields = ('id_news','user_name','comment_text',)


class TegSerializer(ModelSerializer):
    class Meta:
        model = NewsTag
        fields = ('tag_text',)

# сериализатор для просмотра новостей
class NewsSerializer(ModelSerializer):
    tag = TegSerializer(read_only=True,)
    news_author = AuthorSerializer()
    category_name = CategorySerializer(read_only=True,)
    class Meta:
        model = News
        fields = ('news_name','news_author','news_relize_date','news_text','category_name','tag',)


# сериализатор для добавления новостей
class NewsPostSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = ('news_name','news_author','news_relize_date','news_text','category_name','tag',)




