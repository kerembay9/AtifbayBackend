# Generated by Django 4.1.3 on 2022-11-15 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(blank=True, max_length=511, null=True)),
                ('link', models.URLField(blank=True, max_length=511, null=True)),
                ('explanation', models.CharField(blank=True, max_length=5095)),
                ('adddate', models.DateField(auto_now_add=True)),
                ('total_views', models.IntegerField(default=0)),
            ],
        ),
    ]