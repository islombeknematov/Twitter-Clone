# Generated by Django 4.0 on 2021-12-29 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_userprofilemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilemodel',
            name='picture',
            field=models.ImageField(blank=True, default='media/profile_photos/default_image.png', upload_to='media/profile_photos'),
        ),
    ]