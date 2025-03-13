import datetime
from haystack import indexes
from .models import WorkExperience


class WorkExperienceIndex(indexes.SearchIndex, indexes.Indexable):
    company = indexes.CharField(model_attr='company')
    text = indexes.CharField(document=True, model_attr='description')
    name  = indexes.CharField(model_attr='name')
    from_date = indexes.DateTimeField(model_attr='from_date')
    to_date = indexes.DateTimeField(model_attr='to_date')


    def get_model(self):
        return WorkExperience

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects