from elasticsearch import Elasticsearch
from django.conf import settings
from django.core import serializers
import json

es = Elasticsearch(settings.ELASTICSEARCH_CONN)


class ElasticSearchApp:
    def __init__(self, index, doc_type):
        self.index = index
        self.doc_type = doc_type

    def add_article(self, article_doc):
        val = json.loads(serializers.serialize('json', [article_doc,]))[0]
        es.index(index=self.index,doc_type=self.doc_type,id=article_doc.id,body=val["fields"])

    def search_article(self, request):
        response = es.search(index=self.index, body=request)
        return response['hits']['hits']