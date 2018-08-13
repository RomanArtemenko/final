from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as view_auth
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view


from . import views


API_TITLE = 'Article API'
API_DESCRIPTION = 'A Web API for viewing.'

schema_view = get_swagger_view(title=API_TITLE)

router = DefaultRouter()
router.register(r'articles', views.ArticleModelViewSet)
router.register(r'period', views.PeriodModelViewSet)

urlpatterns = [
    path('', views.index , name='index'),
    path('run', views.RunView.as_view(), name='run'),
    path('api/v1.0/', include(router.urls)),
    path('api/v1.0/map/', schema_view, name='map-api'),
    path('api/v1.0/docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
]
