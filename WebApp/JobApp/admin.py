import models
from django.contrib import admin

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Job)
admin.site.register(models.Grade)
admin.site.register(models.Competency)
admin.site.register(models.Has_Grade)
admin.site.register(models.Has_Competency)
admin.site.register(models.Need_Grade)
admin.site.register(models.Need_Competency)
