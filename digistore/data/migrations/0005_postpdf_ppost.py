# Generated by Django 3.0.8 on 2020-09-04 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_post_guser'),
    ]

    operations = [
        migrations.CreateModel(
            name='pPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('guser', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Postpdf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to='files/')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='data.pPost')),
            ],
        ),
    ]