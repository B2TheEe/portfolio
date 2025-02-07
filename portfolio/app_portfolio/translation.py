from modeltranslation.translator import register, TranslationOptions
from .models import PortfolioItem

@register(PortfolioItem)
class PortfolioItemTranslationOptions(TranslationOptions):
    fields = ('description',)