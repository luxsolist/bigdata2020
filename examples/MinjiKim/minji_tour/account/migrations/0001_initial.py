# Generated by Django 3.0.8 on 2020-10-05 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.CharField(max_length=12, primary_key=True, serialize=False, unique=True, verbose_name='아이디')),
                ('password', models.CharField(max_length=12, verbose_name='비밀번호')),
                ('gender', models.CharField(max_length=2, verbose_name='성별')),
                ('age', models.IntegerField(verbose_name='나이')),
                ('address', models.CharField(max_length=255, verbose_name='주소')),
                ('like1', models.CharField(max_length=255, verbose_name='좋아하는 여행지1')),
                ('like2', models.CharField(max_length=255, verbose_name='좋아하는 여행지2')),
                ('like3', models.CharField(max_length=255, verbose_name='좋아하는 여행지3')),
            ],
        ),
    ]
