import datetime

from django.db import models

# Create your models here.
class NewsAuthor(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=20)
    last_name = models.CharField(verbose_name='Фамилия', max_length=20)
    mid_name = models.CharField(verbose_name='Отчество', max_length=20, blank=True)

    def __str__(self):
        return f' {self.first_name}, {self.mid_name}, {self.last_name}'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class NewsCategory(models.Model):
    name = models.CharField(verbose_name='Название', max_length=150)
    description = models.CharField(verbose_name='Описание', max_length=50)

    def __str__(self):
        return f'{self.name}, {self.description}'

    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'





# написать модель тегов
class NewsTag(models.Model):
    tag_text = models.TextField(verbose_name='Текст тега')

    def __str__(self):
        return f' {self.tag_text}'

    class Meta:
        verbose_name ='Тег'
        verbose_name_plural ='Теги'


#После новой модели сделать миграцию python mange.py makemigartions --> python mange.py migrate
class News(models.Model):
    news_author = models.ForeignKey(NewsAuthor,related_name='author' , verbose_name='Автор', on_delete=models.CASCADE)
    news_name = models.CharField(verbose_name='Заголоков', max_length=150)
    news_text = models.TextField(verbose_name='Текст новости')
    news_relize_date = models.DateField(verbose_name='Дата выпуска', default=datetime.date.today())
    category_name = models.ForeignKey(NewsCategory,related_name='category_name', verbose_name='Категория', on_delete=models.CASCADE, null=True)
    tag = models.ForeignKey(NewsTag,related_name='tag' ,verbose_name='Теги', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.news_name},{self.news_author},{self.news_relize_date},{self.news_text},{self.tag},'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class NewsComment(models.Model):
    id_news = models.ForeignKey(News, verbose_name='Новость', on_delete=models.CASCADE)
    comment_text = models.TextField(verbose_name='Текст коментария')
    user_name = models.CharField(verbose_name='Имя пользователя', max_length=50)

    def __str__(self):
        return f' {self.user_name}, {self.comment_text}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
#логин root
#пароль admin


