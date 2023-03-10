# Generated by Django 4.1.5 on 2023-02-16 07:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_tutorial_score_tutorial_slug_tutorial_updated_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tutorial',
            options={'ordering': ('-score',)},
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='slug',
            field=models.SlugField(allow_unicode=True, null=True),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tuts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_reply', models.BooleanField(default=False)),
                ('body', models.TextField(max_length=400)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('approve', models.BooleanField(default=False)),
                ('reply', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rcomments', to='home.comment')),
                ('tut', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tcomments', to='home.tutorial')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ucommens', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
