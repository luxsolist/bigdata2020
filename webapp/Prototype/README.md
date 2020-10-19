# 사용법
===========
### 1. 사전 설정
```console
python manage.py makemigrations
python manage.py migrate
```  
##### 1-1. superuser 설정  
```console
python manage.py createsuperuser
```  
-----------
### 2. db input

##### 2-1. manage.py가 있는 위치에서 다음 명령어 실행  
```console
python manage.py shell
```

##### 2-2. 다음 명령어를 복사 붙여넣기 하여 csv 파일 db에 삽입  
```python
import csv
from tour.models import TourInfo

f = open('a1.csv','r',encoding = 'utf-8')
rdr = csv.reader(f)

for row in rdr:
     print(row)
     TourInfo.objects.create(
              addr1 = row[0],
              areacode = row[1],
              cat1 = row[2],
              cat2 = row[3],
              cat3 = row[4],
              contentid = row[5],
              contenttypeid = row[6],
              createdtime = row[7],
              firstimage = row[8],
              firstimage2 = row[9],
              mapx = row[10],
              mapy = row[11],
              mlevel = row[12],
              modifiedtime = row[13],
              readcount = row[14],
              sigungucode = row[15],
              title = row[16],
              zipcode = row[17],
   )
```
-----------
### 3. 서버 구동  
```console
python manage.py runserver
```
