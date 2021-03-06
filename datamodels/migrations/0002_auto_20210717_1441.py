# Generated by Django 3.2.5 on 2021-07-17 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamodels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facebookfriend',
            name='liked_songs',
            field=models.ManyToManyField(blank=True, related_name='facebook_friends', to='datamodels.LikedSong'),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='facebook_friends',
            field=models.ManyToManyField(blank=True, related_name='recommendations', to='datamodels.FacebookFriend'),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='twitter_experts',
            field=models.ManyToManyField(blank=True, related_name='recommendations', to='datamodels.TwitterExpert'),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='wiki_items',
            field=models.ManyToManyField(blank=True, related_name='recommendations', to='datamodels.WikiItem'),
        ),
        migrations.AlterField(
            model_name='twitterexpert',
            name='liked_songs',
            field=models.ManyToManyField(blank=True, related_name='twitter_experts', to='datamodels.LikedSong'),
        ),
        migrations.AlterField(
            model_name='wikiitem',
            name='liked_songs',
            field=models.ManyToManyField(blank=True, related_name='wiki_items', to='datamodels.LikedSong'),
        ),
    ]
