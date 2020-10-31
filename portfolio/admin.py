from django.contrib import admin
from .models import Services, Certificats, Languages,  Softwars, Principles
# Register your models here.
admin.site.register(Services)
admin.site.register(Certificats)
admin.site.register(Languages)
admin.site.register(Softwars)
admin.site.register(Principles)