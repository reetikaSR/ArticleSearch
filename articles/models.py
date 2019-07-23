from django.db import models
from django.conf import settings
from .ElasticSearch import ElasticSearchApp

el = ElasticSearchApp(settings.ELASTICSEARCH_INDEX, settings.ELASTICSEARCH_DOC)


class Article(models.Model):
    content = models.CharField(max_length=10000)
    authors = models.CharField(max_length=1000)
    locations = models.CharField(max_length=1000)
    tags = models.CharField(max_length=1000)
    categories = models.CharField(max_length=1000)

    def save(self, *args, **kwargs):
        super(Article, self).save(*args, **kwargs)
        el.add_article(self)