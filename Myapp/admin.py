from django.contrib import admin
from .models import *
# Register your models here.
class showlogin(admin.ModelAdmin):
    list_display = ["NAME","EMAIL","PHONE","PASSWORD","profilepic","TIMESTAMP"]
admin.site.register(LOGIN,showlogin)

class showcategory(admin.ModelAdmin):
    list_display = ["CATNAME","catimg"]
admin.site.register(CATEGORY,showcategory)

class showproduct(admin.ModelAdmin):
    list_display = ["CATID","NAME","MATERIAL_TYPE","COLOR","PRICE","DESCRIPTION","QUANTITY","proimg","STATUS"]
admin.site.register(PRODUCT,showproduct)

class showproductimg(admin.ModelAdmin):
    list_display = ["PRODUCTID","photos"]
admin.site.register(PRODUCTIMAGE,showproductimg)

class showinquiry(admin.ModelAdmin):
    list_display = ["PRODUCTID","USERID","QUANTITY","BUDGET","MESSAGE","INQUIRYSTATUS","TIMESTAMP"]
admin.site.register(PRODUCTINQUIRY,showinquiry)

class showcontact(admin.ModelAdmin):
    list_display = ["NAME","EMAIL","PHONE","MESSAGE","TIMESTAMP"]
admin.site.register(CONTACT,showcontact)

class showfeedback(admin.ModelAdmin):
    list_display = ["name","productid","message"]
admin.site.register(feedback,showfeedback)