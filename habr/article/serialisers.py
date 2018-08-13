from rest_framework import serializers
from .models import Article, Period

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'avatar', 'name', 'description', 'keywords', 'url', 'date')


class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = ('begin_time', 'end_time')