from modeltranslation.translator import register, TranslationOptions
from .models import EducationExperience

@register(EducationExperience)
class EducationExperienceTranslationOptions(TranslationOptions):
    fields = ('description',)