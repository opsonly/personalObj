# Generated by Django 2.1.7 on 2019-03-08 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='loveclass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lovecate', models.CharField(max_length=100)),
                ('loveimg', models.ImageField(blank=True, upload_to='lover/%Y%m%d/')),
            ],
        ),
    ]