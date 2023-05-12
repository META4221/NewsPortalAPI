from django.contrib import admin

from NewsPortal.models import NewsAuthor, NewsTag, NewsComment, NewsCategory, News

# Register your models here.
admin.site.register(NewsAuthor)
admin.site.register(NewsTag)
admin.site.register(NewsComment)
admin.site.register(NewsCategory)
admin.site.register(News)
