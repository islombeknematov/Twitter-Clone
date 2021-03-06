# Generated by Django 4.0 on 2022-01-22 10:18

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0015_alter_postmodel_body_alter_postmodel_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='dislike',
            field=models.ManyToManyField(blank=True, related_name='dislike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post_photo'),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='like', to=settings.AUTH_USER_MODEL),
        ),
    ]
