# Generated by Django 3.1.7 on 2021-03-25 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0004_auto_20210325_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='txf',
            field=models.TextField(blank=True, null=True, verbose_name='txf'),
        ),
    ]
