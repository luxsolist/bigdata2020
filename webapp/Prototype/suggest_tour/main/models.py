from django.db import models

# Create your models here.

class TourlistUser(models.Model):
    user_id = models.CharField(primary_key=True, max_length=31)
    user_pw = models.CharField(max_length=63)
    user_name = models.CharField(max_length=31)
    gender = models.CharField(max_length=1)
    email = models.CharField(max_length=63)
    address = models.CharField(max_length=255)
    gps_x = models.FloatField()
    gps_y = models.FloatField()
    create_at = models.DateTimeField(db_column='CREATE_at')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tourlist_user'
      
    def __str__(self):
      return self.user_id + ' / ' + self.email