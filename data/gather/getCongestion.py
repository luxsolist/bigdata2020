from urllib.request import urlopen
import json
import csv
import datetime
import pandas as pd

now = datetime.datetime.now()


## x, y 좌표가 포함된 관광지 정보를 데이터프레임으로
## 4000개 선택한 관광지정보 csv 파일을 불러와야함
df = pd.read_csv('C:/rsource2/a1.csv',names=['arr1','areacode','cat1','cat2','cat3','contentid','contenttypeid','createtime','firstimage','firstimage2','mapx','mapy','mlevel','modifiedtime','readcount','sigungucode','title','zipcode'])
df1 = df.loc[:,['title','contentid','mapy','mapx']] 

df1['road_total']=0
df1['congestion_1']=0
df1['congestion_2']=0
df1['congestion_3']=0
df1['congestion_4']=0
df1['congestion_avg']=0.0
df1['congestion_max']=0
df1['measured_at']=''

def save_congestion(count,count1,count2,count3,count4,total,avg,max1,idx):
    for i in range(count):
        df1['congestion_1'][idx] = count1
        df1['congestion_2'][idx] = count2
        df1['congestion_3'][idx] = count3
        df1['congestion_4'][idx] = count4
        df1['congestion_avg'][idx] = avg
        df1['congestion_max'][idx] = max1
        df1['road_total'][idx] = total
        df1['measured_at'][idx] = now.strftime('%Y/%m/%d %H:%M')

def find_max(count1,count2,count3,count4):
    tempMax = max(count1,count2,count3,count4)
    result = 0
    if tempMax == count1:
        result = 1
    elif tempMax == count2:
        result = 2
    elif tempMax == count3:
        result = 3
    elif tempMax == count4:
        result = 4
        
    return result

def get_congestion(lat,lng,idx):
    url = "https://apis.openapi.sk.com/tmap/traffic?version=1&centerLat="+lat+"&centerLon="+lng+"&reqCoordType=WGS84GEO&resCoordType=WGS84GEO&trafficType=AUTO&radius=9&zoomLevel=17&callback=function&appKey=l7xx15dc34d100d94bbeb85d6717a8fa5feb"
    responseBody = urlopen(url).read().decode('utf-8')
    jsonArray = json.loads(responseBody)
    
    count = len(jsonArray.get('features'))
    
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    
    for i in range(count):
        if jsonArray.get('features')[i].get('properties').get('congestion') == 1:
            count1 += 1
        elif jsonArray.get('features')[i].get('properties').get('congestion') == 2:
            count2 += 1
        elif jsonArray.get('features')[i].get('properties').get('congestion') == 3:
            count3 += 1
        elif jsonArray.get('features')[i].get('properties').get('congestion') == 4:
            count4 += 1
            
    total = count1+count2+count3+count4
    avg = round((count1+(count2*2)+(count3*3)+(count4*4))/total,4)
    max1 = find_max(count1,count2,count3,count4)
    
    # print("혼잡도 1: ",count1,'혼잡도 2: ',count2,'혼잡도 3: ',count3,'혼잡도 4: ',count4 ,'총 : ',total)
    
    save_congestion(count,count1,count2,count3,count4,total,avg,max1,idx)

for idx in range(len(df1)):
    try:
        # print(df1['title'][idx])
        get_congestion(str(df1['mapy'][idx]),str(df1['mapx'][idx]),idx)
    except:
        print('error')

df2 = df1.loc[:,['title','contentid','congestion_1','congestion_2','congestion_3','congestion_4','congestion_avg','congestion_max','road_total','measured_at']]
df2.to_csv('traffic날짜와 시간쓰세요.csv',mode='w',encoding='cp949')