from modeltranslation.translator import register, TranslationOptions
from .models import WorkExperience

@register(WorkExperience)
class WorkExperienceTranslationOptions(TranslationOptions):
    fields = ( 'name','description',)