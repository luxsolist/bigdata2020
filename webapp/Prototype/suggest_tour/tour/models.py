from django.db import models

class TOURLIST_SITE(models.Model):
    tour_id = models.IntegerField(primary_key=True, blank=False)
    title = models.CharField(max_length=255, blank=False)
    cat1 = models.CharField(max_length=3, blank=False)
    cat2 = models.CharField(max_length=5, blank=False)
    cat3 = models.CharField(max_length=9, blank=False)
    areacode = models.IntegerField(default=0)
    addr1 = models.CharField(max_length=255)
    tel = models.CharField(max_length=31)
    mapx = models.FloatField(default=0.0, blank=False)
    mapy = models.FloatField(default=0.0, blank=False)
    firstimage = models.CharField(max_length=255)
    firstimage2 = models.CharField(max_length=255)
    contentid = models.IntegerField(blank=False)
    contenttypeid = models.IntegerField(blank=False)
    readcount = models.IntegerField(default=0)
    sigungucode = models.IntegerField(default=0)
    zipcode = models.IntegerField(default=0)

    def __str__(self):
        return self.title

# class TOURLIST_TRAFFIC(models.Model):
#     tour_id = models.ForeignKey