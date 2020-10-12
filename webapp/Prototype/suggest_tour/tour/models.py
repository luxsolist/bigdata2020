from django.db import models

class TourInfo(models.Model):
    addr1 = models.CharField(max_length=400)
    areacode = models.CharField(max_length=255)
    cat1 = models.CharField(max_length=255)
    cat2 = models.CharField(max_length=255)
    cat3 = models.CharField(max_length=255)
    contentid = models.IntegerField() #pk로 할까 생각중
    contenttypeid =models.IntegerField()
    createdtime = models.IntegerField()
    firstimage = models.CharField(max_length=255)
    firstimage2 = models.CharField(max_length=255)
    mapx = models.CharField(max_length=255)
    mapy = models.CharField(max_length=255)
    mlevel = models.IntegerField()
    modifiedtime = models.IntegerField()
    readcount = models.IntegerField()
    sigungucode = models.IntegerField()
    title = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)

    def __str__(self):
        return self.title

