import datetime
from haystack import indexes
from .models import Skill, Category


class SkillIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, model_attr='description')
    rating = indexes.IntegerField(model_attr='rating')
    skill = indexes.CharField(model_attr='skill')


    def get_model(self):
        return Skill

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects


class CategoryIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, model_attr='name')

    def get_model(self):
        return Category

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects