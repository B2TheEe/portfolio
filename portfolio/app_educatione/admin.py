from django.contrib import admin
from .models import EducationExperience

# Register your models here.
""" 
class EducationExperienceAdmin(admin.ModelAdmin):
    class Meta:
        model = EducationExperience
        fields = ('photo', 'company', ' name', 'description', 'from_date ','to_date','Propaedeutic_exam_date', 'degree_date')

    def __init__(self, *args, **kwargs):
        super(EducationExperienceAdmin, self).__init__(*args, **kwargs)
        #self.fields['Propaedeutic_exam_date'].required = False
       # self.fields['degree_date'].required = False
       """
admin.site.register(EducationExperience)