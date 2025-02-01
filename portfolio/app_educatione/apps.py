from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class EducationeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_educatione'
    verbose_name = _('app_educatione')
