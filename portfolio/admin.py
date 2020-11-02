from django.contrib import admin
from .models import Service, Certificat, Language,  Softwar, Principle, LangCat, PrinCat, SofCat, CertCat
# Register your models here.
admin.site.register(Service)
admin.site.register(Certificat)
admin.site.register(Language)
admin.site.register(Softwar)
admin.site.register(Principle)
admin.site.register(CertCat)
admin.site.register(LangCat)
admin.site.register(SofCat)
admin.site.register(PrinCat)