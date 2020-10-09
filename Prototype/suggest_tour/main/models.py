from django.db import models

# Create your models here.


class Accounts(models.Model):
  account_id = models.AutoField('account_id', primary_key=True)
  user_id = models.CharField(max_length=20)
  user_pw = models.CharField(max_length=16)
  user_name = models.CharField(max_length=20)
  gender = models.IntegerField(default=None)
  email = models.EmailField(default = None)
  address = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    db_table = 'accounts'

  def __str__(self):
    return self.user_id + ' / ' + self.email