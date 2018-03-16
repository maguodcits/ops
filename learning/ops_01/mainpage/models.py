from django.db import models
import django.utils.timezone as timezon


# Create your models here.
#
class PowerSetting(models.Model):
    powerName=models.CharField(max_length=100)
    powerIP=models.CharField(max_length=50)
    powerNumber=models.CharField(max_length=10)
    powerUsername=models.CharField(max_length=50)
    powerPassword=models.CharField(max_length=300)
    add_date = models.DateTimeField('保存日期', default=timezon.now)
    mod_date = models.DateTimeField('最后修改日期', auto_now=True)
    # def __str__(self):
    #     # return  self.powerName,self.powerIP
    #     return "{},{},{},{}".format(self.powerName, self.powerIP,self.powerNumber,self.powerUsername)
