from modeltranslation.translator import register, TranslationOptions
from .models import Category,Skill

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Skill)
class SkillTranslationOptions(TranslationOptions):
    fields = ( 'skill' ,)