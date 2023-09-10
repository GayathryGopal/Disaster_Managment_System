from django.contrib import admin
from flood.models import floods,form,regist

# Register your models here.
class rain(admin.ModelAdmin):
    list_display=('Camp_id','Camp_Name','img')
admin.site.register(floods,rain)
class formadmin(admin.ModelAdmin):
    list_display=('Camp_Id','Name','Address','Age')
admin.site.register(form,formadmin)
class registadmin(admin.ModelAdmin):
    list_display=('Camp_Id','Product','Quantity')
admin.site.register(regist,registadmin)