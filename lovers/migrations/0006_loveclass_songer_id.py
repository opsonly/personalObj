# Generated by Django 2.1.7 on 2019-03-14 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lovers', '0005_songcomment_comment_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='loveclass',
            name='songer_id',
            field=models.IntegerField(default=0),
        ),
    ]
