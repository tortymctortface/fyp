# Generated by Django 3.1.7 on 2021-03-08 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210308_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='palace',
            name='trigger_words',
            field=models.CharField(blank=True, max_length=5000),
        ),
    ]
