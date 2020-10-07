from django.db import models
# from django.contrib.auth.models import UserForm

class User(models.Model):
    username = models.CharField('아이디',primary_key=True, max_length = 12, unique = True)
    password = models.CharField('비밀번호',max_length =12)
    gender = models.CharField('성별',max_length =2)
    age = models.IntegerField('나이')
    address = models.CharField('주소',max_length =255)
    like1 = models.CharField('좋아하는 여행지1',max_length =255)
    like2 = models.CharField('좋아하는 여행지2',max_length =255)
    like3 = models.CharField('좋아하는 여행지3',max_length =255)

    USERNAME_FIELD = 'username' # 아이디를 사용자 식별자로 설정
    # REQUIRED_FIELDS = ['email'] # 필수입력값

    def __str__(self):
        return self.username