# Generated by Django 3.1.2 on 2020-10-13 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_post_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(null=True, upload_to='media/upload/%Y/%m/%d/'),
        ),
    ]