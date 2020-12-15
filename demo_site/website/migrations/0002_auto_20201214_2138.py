# Generated by Django 2.2 on 2020-12-15 02:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='user_likes',
            field=models.ManyToManyField(blank=True, null=True, related_name='liked_blogs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_replies', to='website.Comment')),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_replies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='blog_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_comment', to='website.Blog'),
        ),
        migrations.AddField(
            model_name='comment',
            name='poster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
