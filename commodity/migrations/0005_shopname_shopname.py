# Generated by Django 2.1.7 on 2019-03-01 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commodity', '0004_shopname_commonname'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopname',
            name='shopname',
            field=models.CharField(default='小熊家的店', max_length=100),
        ),
    ]
