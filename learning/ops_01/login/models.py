from django.db import models
import django.utils.timezone as timezon
# Create your models here.
class UserInput(models.Model):
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=32)
    add_date = models.DateTimeField('保存日期', default=timezon.now)
    mod_date = models.DateTimeField('最后修改日期', auto_now=True)
    def __str__(self):
        return self.username
