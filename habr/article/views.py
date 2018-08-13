from django.shortcuts import render, redirect
from .models import Article, Period
from .serialisers import ArticleSerializer, PeriodSerializer
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from django.views.generic import View
from django.conf import settings
import redis

redis_server = redis.Redis(settings.REDIS_HOST, settings.REDIS_PORT)

# Create your views here.

def index(request):
    articles = Article.objects.all()
    return render(request, 'article/index.html', {'articles':articles})

class ArticleModelViewSet(ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class PeriodModelViewSet(ModelViewSet):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
        
class RunView(View):
    template_name = 'article/run.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        redis_server.lpush('habr:start_urls', 'https://habr.com')
        return redirect('index')

