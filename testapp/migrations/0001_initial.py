# Generated by Django 2.2 on 2020-11-30 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=1000)),
                ('exp', models.IntegerField()),
                ('prev_cmpny', models.CharField(max_length=25)),
                ('applyng_role', models.CharField(max_length=25)),
                ('pic', models.ImageField(upload_to='iamges')),
                ('document', models.FileField(upload_to='documents')),
                ('n_p', models.IntegerField()),
            ],
        ),
    ]
