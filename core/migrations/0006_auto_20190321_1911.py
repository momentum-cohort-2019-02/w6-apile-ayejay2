# Generated by Django 2.1.7 on 2019-03-21 23:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_merge_20190321_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='posted_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
