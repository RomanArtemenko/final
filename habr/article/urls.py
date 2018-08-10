from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls

from . import views
from .views import ArticleModelViewSet

schema_view = get_swagger_view(title='Pastebin API')

API_TITLE = 'Article API'
API_DESCRIPTION = 'A Web API for viewing.'

schema_view = get_swagger_view(title=API_TITLE)

router = DefaultRouter()
router.register(r'articles', views.ArticleModelViewSet)

urlpatterns = [
    path('', views.index , name='index'),
    url(r'api/v1.0/', include(router.urls)),
    path('api/v1.0/map/', schema_view, name='map-api'),
    path('api/v1.0/docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
]