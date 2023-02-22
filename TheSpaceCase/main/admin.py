from django.contrib import admin
from .models import Contact,Company,Certificate,Post
# Register your models here.


#to customize the panel
class ContactAdmin(admin.ModelAdmin):
    list_display = ()


class CompanyAdmin(admin.ModelAdmin):
    list_display = ()


class CertificateAdmin(admin.ModelAdmin):
    list_display = ()


class PostAdmin(admin.ModelAdmin):
    list_display = ()



admin.site.register(Contact,ContactAdmin)
admin.site.register(Company,CompanyAdmin)
admin.site.register(Certificate,CertificateAdmin)
admin.site.register(Post,PostAdmin)
