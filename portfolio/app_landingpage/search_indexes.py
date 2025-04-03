from haystack import indexes
from .models import LandingPage


class LandingPageIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, model_attr='about')



    def get_model(self):
        return LandingPage

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects