from django.db import models
from django.utils.safestring import mark_safe

STATUS_LIST = {
    ("1","Available"),
    ("0","Not Available")
}
# Create your models here.
class LOGIN(models.Model):
    NAME = models.CharField(max_length=60)
    EMAIL = models.EmailField()
    PHONE = models.BigIntegerField()
    PASSWORD = models.CharField(max_length=50)
    dp = models.ImageField(upload_to='upic',null=True)
    TIMESTAMP = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.NAME

    def profilepic(self):
        return mark_safe('<img src = "{}" width = "100">'.format(self.dp.url))
    profilepic.allow_tags = True


class CATEGORY(models.Model):
    CATNAME = models.CharField(max_length=70)
    CATIMAGE = models.ImageField(upload_to='catimg',null=True)

    def catimg(self):
        return mark_safe('<img src = "{}" width = "100">'.format(self.CATIMAGE.url))
    catimg.allow_tags = True

    def __str__(self):
        return self.CATNAME

class PRODUCT(models.Model):
    CATID = models.ForeignKey(CATEGORY,on_delete=models.CASCADE)
    NAME = models.CharField(max_length=100)
    MATERIAL_TYPE = models.CharField(max_length=100)
    COLOR = models.CharField(max_length=50)
    PRICE = models.FloatField()
    DESCRIPTION = models.TextField()
    QUANTITY = models.IntegerField()
    IMAGE = models.ImageField(upload_to='proimg',null=True)
    STATUS = models.CharField(choices=STATUS_LIST,max_length=60)

    def proimg(self):
        return mark_safe('<img src = "{}" width = "100">'.format(self.IMAGE.url))
    proimg.allow_tags = True

    def __str__(self):
        return self.NAME

class PRODUCTIMAGE(models.Model):
    PRODUCTID = models.ForeignKey(PRODUCT,on_delete=models.CASCADE)
    IMAGE = models.ImageField(upload_to='proimg',null=True)

    def photos(self):
        return mark_safe('<img src = "{}" width = "100">'.format(self.IMAGE.url))
    photos.allow_tags = True

class PRODUCTINQUIRY(models.Model):
    PRODUCTID = models.ForeignKey(PRODUCT,on_delete=models.CASCADE)
    USERID = models.ForeignKey(LOGIN,on_delete=models.CASCADE)
    QUANTITY = models.IntegerField()
    BUDGET = models.FloatField()
    MESSAGE = models.TextField()
    INQUIRYSTATUS = models.CharField(max_length=100)
    TIMESTAMP = models.DateTimeField(auto_now=True)

class CONTACT(models.Model):
    NAME = models.CharField(max_length=60)
    EMAIL = models.EmailField()
    PHONE = models.BigIntegerField()
    MESSAGE = models.TextField()
    TIMESTAMP = models.DateTimeField(auto_now=True)

class feedback(models.Model):
    name = models.CharField(max_length=60)
    productid = models.ForeignKey(PRODUCT,on_delete=models.CASCADE)
    message = models.TextField()
