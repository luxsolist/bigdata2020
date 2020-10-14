from django.db import models

# Create your models here.


class TOURLIST_USER(models.Model):
  user_id = models.CharField(max_length = 31, primary_key = True, blank=False)
  user_pw = models.CharField(max_length = 63, blank = False)
  user_name = models.CharField(max_length = 31, blank = False)
  gender = models.CharField(max_length = 1, blank = False)
  email = models.CharField(max_length = 63, blank = False)
  address = models.CharField(max_length = 255, blank = False)
  gps_x = models.FloatField(default = 0.0, blank = False)
  gps_y = models.FloatField(default = 0.0, blank = False)
  created_at = models.DateTimeField(auto_now_add = True)

  # account_id = models.AutoField('account_id', primary_key=True)
  # user_id = models.CharField(max_length=20)
  # user_pw = models.CharField(max_length=16)
  # user_name = models.CharField(max_length=20)
  # gender = models.IntegerField(default=None)
  # email = models.EmailField(default = None)
  # address = models.CharField(max_length=100)
  # created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    db_table = 'TOURLIST_USER'

  def __str__(self):
    return self.user_id + ' / ' + self.email