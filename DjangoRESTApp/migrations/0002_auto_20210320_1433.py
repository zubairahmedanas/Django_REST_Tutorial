# Generated by Django 3.1.5 on 2021-03-20 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoRESTApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
