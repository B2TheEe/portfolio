import datetime
from haystack import indexes
from .models import PortfolioItem


class PortfolioItemIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, model_attr='description')
    gitHubUrl = indexes.CharField(model_attr='gitHubUrl')
    name = indexes.CharField(model_attr='name')


    def get_model(self):
        return PortfolioItem

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects