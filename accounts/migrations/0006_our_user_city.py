# Generated by Django 2.2.5 on 2019-09-19 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20190919_0506'),
    ]

    operations = [
        migrations.AddField(
            model_name='our_user',
            name='city',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
