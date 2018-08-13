from .models import Article
from habr.celery import app
import json

@app.task
def add_item(item):
    
    item = json.loads(item)
    Article.objects.get_or_create(
        avatar=item['avatar'],
        name=item['name'],
        description=item['description'],
        keywords=item['keywords'],
        url=item['url'],
        date=item['date'],
    )
