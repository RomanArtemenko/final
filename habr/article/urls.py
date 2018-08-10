from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from . import views
from .views import ArticleModelViewSet

router = DefaultRouter()
router.register(r'articles', views.ArticleModelViewSet)

urlpatterns = [
    path('', views.index , name='index'),
    url(r'api/v1.0/', include(router.urls)),
]