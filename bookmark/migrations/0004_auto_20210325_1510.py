# Generated by Django 3.1.7 on 2021-03-25 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0003_auto_20210325_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='dtf',
            field=models.DateTimeField(blank=True, null=True, verbose_name='DTF'),
        ),
    ]
