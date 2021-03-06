# 사용법
---
### 1. mysqlclient 설치
```console
pip install django
pip install mysqlclient
pip install haversine
pip install pandas
pip install sqlalchemy
pip install sklearn
```

### 2. DB 생성 및 csv파일 데이터 넣기
- C:\bigdata2020\webapp\Prototype\쿼리문.sql 사용
- tour_id 0번 삭제 (마리아DB에서 임의로 들어가서 삭제필요)
- tour_data중 10개의 데이터가 제대로 입력되지않아 수기입력 필요 (tour_except.csv)
```
mysql -u root -p < 쿼리문.sql
```

### 3. DB 접속 정보 변경
./suggest_tour/settings.py 변경
```console
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'TourList',
        'USER': 'root',         # 설치 당시 본인이 생성한 USER. default는 root
        'PASSWORD': 'admin1234',     # 설치 당시 설정한 비밀번호.
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

./tour/recommender.py 변경
```console
def recommend():
  # sql 호출, 데이터 불러오기
  engine = create_engine("mysql://root:admin1234@localhost:3306/Tourlist")
```

##### 3-1. superuser 설정
```console
python manage.py migrate
python manage.py createsuperuser
```  

### 4. 서버 구동하여 확인 
```console
python manage.py runserver
```
http://localhost:8000/tour/  에서 DB연동 확인가능 
