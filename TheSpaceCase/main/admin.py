from django.contrib import admin
from .models import Contact,Company,Certificate,Post,ApplyContent
# Register your models here.


#to customize the panel
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','subject')


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name','website')


class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name','certificate_id')


class PostAdmin(admin.ModelAdmin):
    list_display = ('title','created_date','company')

class ApplyContentAdmin(admin.ModelAdmin):
    list_display = ('name','email','title','company')


admin.site.register(Contact,ContactAdmin)
admin.site.register(Company,CompanyAdmin)
admin.site.register(Certificate,CertificateAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(ApplyContent,ApplyContentAdmin)
