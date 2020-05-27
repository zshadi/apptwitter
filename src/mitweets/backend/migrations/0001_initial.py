# Generated by Django 3.0.5 on 2020-05-09 00:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TweeterUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('screen_name', models.CharField(max_length=50, unique=True)),
                ('tweeter_id', models.CharField(max_length=50, unique=True)),
                ('url', models.URLField(unique=True)),
                ('location', models.TextField()),
                ('image_url', models.URLField()),
                ('banner_url', models.URLField()),
                ('description', models.TextField()),
                ('n_followers', models.IntegerField()),
                ('n_tweets', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet_id', models.CharField(max_length=50, unique=True)),
                ('created_at', models.DateTimeField()),
                ('text', models.TextField()),
                ('n_replies', models.IntegerField()),
                ('n_retweet', models.IntegerField()),
                ('n_favorite', models.IntegerField()),
                ('language', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('url', models.URLField(unique=True)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('screen_name', models.CharField(max_length=50, unique=True)),
                ('tweeter_id', models.CharField(max_length=50, unique=True)),
                ('tweeter_url', models.URLField(unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='')),
                ('bio', models.TextField(blank=True, null=True)),
                ('gender', models.IntegerField(choices=[(0, 'Female'), (1, 'Male'), (2, 'Other')])),
                ('location', models.TextField(blank=True, null=True)),
                ('website', models.URLField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
