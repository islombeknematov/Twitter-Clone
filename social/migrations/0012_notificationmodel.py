# Generated by Django 4.0 on 2022-01-08 09:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('social', '0011_commentmodel_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_type', models.IntegerField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user_has_seen', models.BooleanField(default=False)),
                ('comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='social.commentmodel')),
                ('from_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notification_from', to='auth.user')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='social.postmodel')),
                ('to_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notification_to', to='auth.user')),
            ],
            options={
                'verbose_name': 'notification',
                'verbose_name_plural': 'notifications',
            },
        ),
    ]
