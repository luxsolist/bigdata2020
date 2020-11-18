# Generated by Django 3.1.2 on 2020-11-17 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalysisReseult',
            fields=[
                ('tour_id', models.IntegerField(primary_key=True, serialize=False)),
                ('readcount_score', models.FloatField()),
                ('congestion_score', models.FloatField()),
                ('star_score', models.FloatField()),
                ('senti_word', models.TextField()),
                ('senti_count', models.IntegerField()),
                ('senti_sum', models.IntegerField()),
                ('senti_avg', models.FloatField()),
                ('corona_score', models.FloatField()),
                ('spring', models.FloatField()),
                ('summer', models.FloatField()),
                ('fall', models.FloatField()),
                ('winter', models.FloatField()),
            ],
            options={
                'db_table': 'ANALYSIS_RESULT',
                'managed': False,
            },
        ),
        migrations.AlterModelTable(
            name='tourlistsite',
            table='TOURLIST_SITE',
        ),
        migrations.AlterModelTable(
            name='tourlisttraffic',
            table='TOURLIST_TRAFFIC',
        ),
    ]
