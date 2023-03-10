# Generated by Django 4.1.5 on 2023-02-14 08:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
