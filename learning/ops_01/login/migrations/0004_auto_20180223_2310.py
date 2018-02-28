# Generated by Django 2.0.2 on 2018-02-23 15:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20180223_2300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinput',
            name='last_login',
        ),
        migrations.AddField(
            model_name='userinput',
            name='add_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='保存日期'),
        ),
        migrations.AddField(
            model_name='userinput',
            name='mod_date',
            field=models.DateTimeField(auto_now=True, verbose_name='最后修改日期'),
        ),
    ]
