# Generated by Django 3.2 on 2022-01-13 18:40

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
            name='Coins',
            fields=[
                ('coin_id', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('coin_name', models.CharField(max_length=200)),
                ('coin_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('market_cap', models.DecimalField(decimal_places=0, max_digits=12)),
                ('rank', models.IntegerField()),
                ('price_change', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_coin', to='app.coins')),
                ('down_votes', models.ManyToManyField(blank=True, related_name='post_down_votes', to=settings.AUTH_USER_MODEL)),
                ('up_votes', models.ManyToManyField(blank=True, related_name='post_up_votes', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_coin_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('down_votes', models.ManyToManyField(blank=True, related_name='comment_down_votes', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='app.coins')),
                ('up_votes', models.ManyToManyField(blank=True, related_name='comment_up_votes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]