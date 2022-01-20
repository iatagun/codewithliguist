# Generated by Django 3.2.6 on 2021-08-14 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonetic', models.BooleanField(default=False, verbose_name='Fonetik Yaz (G2P)')),
                ('harmony', models.BooleanField(default=False, verbose_name='Ünlü Uyumu')),
                ('syllableH', models.BooleanField(default=False, verbose_name='Seslemlere Ayır')),
                ('syllableM', models.BooleanField(default=False, verbose_name='Seslemlere Ayır (Dönüştürür)')),
                ('syllableCount', models.BooleanField(default=False, verbose_name='Seslem Örüntülerini Say')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
    ]
