import datetime
from haystack import indexes
from .models import AboutMe


class AboutMeIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, model_attr='about_me')
    name = indexes.CharField(model_attr='name')


    def get_model(self):
        return AboutMe

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects