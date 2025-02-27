import datetime
from haystack import indexes
from .models import EducationExperience


class EducationExperienceIndex(indexes.SearchIndex, indexes.Indexable):
    company = indexes.CharField(model_attr='company')
    text = indexes.CharField(document=True, model_attr='description')
    name  = indexes.CharField(model_attr='name')
    from_date = indexes.DateTimeField(model_attr='from_date')
    to_date = indexes.DateTimeField(model_attr='to_date')
    propaedeutic_exam_date = indexes.DateTimeField(model_attr='propaedeutic_exam_date',default=None,null=True )
    degree_date = indexes.DateTimeField(model_attr='degree_date',default=None,null=True)

    def get_model(self):
        return EducationExperience

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects