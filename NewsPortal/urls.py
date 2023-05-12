from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

from NewsPortal.views import AuthorViewSet, CategoryViewSet, NewsViewSet, CommentViewSet, TegViewSet

router = DefaultRouter()
router.register('authors', AuthorViewSet)
router.register('Category', CategoryViewSet)
router.register('News', NewsViewSet)
router.register('Comments', CommentViewSet)
router.register('Teg', TegViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]