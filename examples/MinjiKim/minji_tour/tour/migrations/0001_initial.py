# Generated by Django 3.0.8 on 2020-10-05 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TourInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addr1', models.CharField(max_length=400)),
                ('areacode', models.CharField(max_length=255)),
                ('cat1', models.CharField(max_length=255)),
                ('cat2', models.CharField(max_length=255)),
                ('cat3', models.CharField(max_length=255)),
                ('contentid', models.IntegerField()),
                ('contenttypeid', models.IntegerField()),
                ('createdtime', models.IntegerField()),
                ('firstimage', models.CharField(max_length=255)),
                ('firstimage2', models.CharField(max_length=255)),
                ('mapx', models.CharField(max_length=255)),
                ('mapy', models.CharField(max_length=255)),
                ('mlevel', models.IntegerField()),
                ('modifiedtime', models.IntegerField()),
                ('readcount', models.IntegerField()),
                ('sigungucode', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('zipcode', models.CharField(max_length=255)),
            ],
        ),
    ]
