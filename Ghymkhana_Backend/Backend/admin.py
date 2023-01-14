from django.contrib import admin

from Backend.models import meeting
from Backend.models import ugSenator
from Backend.models import pgSenator
from Backend.models import facultyExecutivebodie
from Backend.models import studentExecutivebodie

# Register your models here.
admin.site.register(meeting)
admin.site.register(ugSenator)
admin.site.register(pgSenator)
admin.site.register(facultyExecutivebodie)
admin.site.register(studentExecutivebodie)