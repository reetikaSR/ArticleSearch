from django.test import TestCase
from .ElasticSearch import ElasticSearchApp


# Create your tests here.
class SearchArticleTest(TestCase):
    def setUp(self):
        self.el = ElasticSearchApp('articles', 'article')

    def search_article(self):
        q = {"query":{"match":{"tags":"Django"}}}
        resp = self.el.search_article(q)
        articles = [x['_source'] for x in resp]
        print(articles)