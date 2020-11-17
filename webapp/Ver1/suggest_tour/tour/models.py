from django.db import models

class TourlistSite(models.Model):
    tour_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    cat1 = models.CharField(max_length=3)
    cat2 = models.CharField(max_length=5)
    cat3 = models.CharField(max_length=9)
    areacode = models.IntegerField(blank=True, null=True)
    addr1 = models.CharField(max_length=255, blank=True, null=True)
    tel = models.CharField(max_length=31, blank=True, null=True)
    mapx = models.FloatField()
    mapy = models.FloatField()
    firstimage = models.CharField(max_length=255, blank=True, null=True)
    firstimage2 = models.CharField(max_length=255, blank=True, null=True)
    contentid = models.IntegerField()
    contenttypeid = models.IntegerField()
    readcount = models.IntegerField(blank=True, null=True)
    sigungucode = models.IntegerField(blank=True, null=True)
    zipcode = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TOURLIST_SITE'

    def __str__(self):
        return self.title


class TourlistTraffic(models.Model):
    tour_id = models.OneToOneField(TourlistSite, models.DO_NOTHING, primary_key=True)
    congestion_1 = models.IntegerField()
    congestion_2 = models.IntegerField()
    congestion_3 = models.IntegerField()
    congestion_4 = models.IntegerField()
    congestion_avg = models.FloatField()
    congestion_max = models.FloatField()
    road_count = models.IntegerField()
    measured_at = models.CharField(max_length=31)

    class Meta:
        managed = False
        db_table = 'TOURLIST_TRAFFIC'
        unique_together = (('tour_id', 'measured_at'),)

    def __str__(self):
        return self.tour_id


class AnalysisReseult(models.Model):
    tour_id = models.IntegerField(primary_key=True)
    readcount_score = models.FloatField()
    congestion_score = models.FloatField()
    star_score = models.FloatField()
    senti_word = models.TextField()
    senti_count = models.IntegerField()
    senti_sum = models.IntegerField()
    senti_avg = models.FloatField()
    corona_score = models.FloatField()
    spring = models.FloatField()
    summer = models.FloatField()
    fall = models.FloatField()
    winter = models.FloatField()

    class Meta:
        managed = False
        db_table = 'ANALYSIS_RESULT'
        unique_together = (('tour_id'),)

    def __str__(self):
        return self.tour_id