# Generated by Django 3.0.8 on 2020-08-25 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_post_postimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='guser',
            field=models.CharField(default='deepanshu', max_length=250),
            preserve_default=False,
        ),
    ]