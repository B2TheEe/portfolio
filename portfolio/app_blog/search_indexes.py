import datetime
from haystack import indexes
from .models import BlogArticle


class BlogArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, model_attr='text')
    title = indexes.CharField(model_attr='title')
    date_published = indexes.DateTimeField(model_attr='date_published')

    def get_model(self):
        return BlogArticle

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects