
from modeltranslation.translator import register, TranslationOptions
from .models import AboutMe

@register(AboutMe)
class AboutMeTranslationOptions(TranslationOptions):
    fields = ( 'about_me',)