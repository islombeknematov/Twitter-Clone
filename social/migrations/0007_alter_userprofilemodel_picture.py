# Generated by Django 4.0 on 2021-12-29 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0006_alter_userprofilemodel_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilemodel',
            name='picture',
            field=models.ImageField(blank=True, default='profile_photos/default_image.png', null=True, upload_to='profile_photos'),
        ),
    ]
