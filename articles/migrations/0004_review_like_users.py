# Generated by Django 3.2.13 on 2022-10-24 14:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0003_review_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='like_users',
            field=models.ManyToManyField(related_name='like_articles', to=settings.AUTH_USER_MODEL),
        ),
    ]