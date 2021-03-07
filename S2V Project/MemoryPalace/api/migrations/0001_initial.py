# Generated by Django 3.1.7 on 2021-03-06 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Palace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50, unique=True)),
                ('version', models.IntegerField(default=1)),
                ('second_letter_weight', models.DecimalField(decimal_places=2, default=0.1, max_digits=3)),
                ('phonetic_weight', models.DecimalField(decimal_places=2, default=0.2, max_digits=3)),
                ('theme', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]