# Generated by Django 2.2.7 on 2020-06-04 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200604_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(upload_to='uploads/%Y/%m/%d/'),
        ),
    ]