from django.db import models

class requestform(models.Model):
    name=models.CharField(max_length=50,verbose_name='نام و نام خانوادگی ')
    number=models.IntegerField(verbose_name='شماره تماس')
    email=models.EmailField(verbose_name='ایمیل')
    idcode=models.IntegerField(verbose_name='کد ملی')
    cardnumber=models.IntegerField(verbose_name='شماره کارت')
    pay=models.IntegerField(verbose_name='مبلغ به تومان')
    def __str__(self):
        return self.name

class record(models.Model):
    name=models.CharField(max_length=50,verbose_name='نام و نام خانوادگی ')
    number=models.IntegerField(verbose_name='شماره تماس')
    email=models.EmailField(verbose_name='ایمیل')
    body=models.TextField(verbose_name='پیام')
    def __str__(self):
        return self.name


