# Generated by Django 3.2.5 on 2022-04-02 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_remove_bid_bid_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='bid_author',
            field=models.CharField(max_length=20, null=True),
        ),
    ]