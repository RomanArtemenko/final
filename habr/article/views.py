from django.shortcuts import render
from .models import Article
from .serialisers import ArticleSerializer
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

# Create your views here.

def index(request):
    articles = Article.objects.all()
    return render(request, 'article/index.html', {'articles':articles})

class ArticleModelViewSet(ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer