# Generated by Django 4.1 on 2022-08-26 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ColoursToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.TextField()),
                ('daterandom', models.DateTimeField(auto_now_add=True, verbose_name='Date random')),
            ],
        ),
    ]