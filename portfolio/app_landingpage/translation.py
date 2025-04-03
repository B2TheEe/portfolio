from modeltranslation.translator import register, TranslationOptions
from .models import LandingPage

@register(LandingPage)
class LandingPageTranslationOptions(TranslationOptions):
    fields = ( 'about', 'cv', 'subtitle')