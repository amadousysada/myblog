# Generated by Django 2.2.1 on 2019-11-04 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='topic',
            field=models.TextField(),
        ),
    ]
