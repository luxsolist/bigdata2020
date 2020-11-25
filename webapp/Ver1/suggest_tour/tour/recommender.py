import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from haversine import haversine
from sklearn.preprocessing import MinMaxScaler
import datetime


def recommend(lat, lng, category, dist, congestion):
  # sql 호출, 데이터 불러오기
  engine = create_engine("mysql://admin:1234@localhost:3306/Tourlist")
  tour_data = pd.read_sql("SELECT * FROM TOURLIST_SITE", engine)
  scale_data = pd.read_sql("SELECT * FROM ANALYSIS_RESULT", engine)

  # 가중치
  weight_dist = 0.1
  weight_rc = 0.2
  weight_conavg = 0.15
  weight_sentiavg = 0.15
  weight_starscore = 0.2
  weight_season = 0.1
  weight_covid = 0.1

  cur_location = (lat,lng)

  # gps 좌표로 거리(km) 계산
  scale_data["dist"] = tour_data.apply(lambda x: haversine(cur_location, (x['mapy'], x['mapx'])), axis=1)


  # html에서 받아온 대분류 필터링
  if category == 'A':
    filter_cat = scale_data.loc[(tour_data['cat1'] == 'A01') | (tour_data['cat1'] == 'A02')]
  elif category =='B':
    filter_cat = scale_data.loc[(tour_data['cat1'] == 'A03') | (tour_data['cat1'] == 'A04') | (tour_data['cat1'] == 'A05')]
  elif category =='C':
    filter_cat = scale_data.loc[tour_data['cat1'] == 'B02']
  else:
    filter_cat = scale_data
  
  # 거리 필터링
  filter_dist = filter_cat.loc[filter_cat["dist"] < int(dist, base=10)] if dist !='none' else filter_cat

  # 혼잡도 필터링
  if congestion == 'A':
    filtered_data = filter_dist.loc[filter_dist["congestion_score"] < 0.425635]
  elif congestion == "B":
    filtered_data = filter_dist.loc[filter_dist["congestion_score"] < 0.473350]
  else:
    filtered_data = filter_dist

  # 0~1 사이 값으로 scaling
  scaler = MinMaxScaler()
  try:
    filtered_data[["dist_score"]] = scaler.fit_transform(filtered_data[["dist"]])
  except ValueError:
    return

  # 계절 구하기
  now_month = datetime.datetime.now().month

  if (now_month == 3) | (now_month == 4) | (now_month == 5):
      season = 'spring'
  elif (now_month == 6) | (now_month == 7) | (now_month == 8):
      season = 'summer'
  elif (now_month == 9) | (now_month == 10) | (now_month == 11):
      season = 'fall'
  else :
      season = 'winter'
    
  filtered_data['senti_avg'] = scaler.fit_transform(filtered_data[['senti_avg']])
  
  filtered_data['spring'] = scaler.fit_transform(filtered_data[['spring']])
  filtered_data['summer'] = scaler.fit_transform(filtered_data[['summer']])
  filtered_data['fall'] = scaler.fit_transform(filtered_data[['fall']])
  filtered_data['winter'] = scaler.fit_transform(filtered_data[['winter']])

  # weight 계산
  filtered_data['dist_cost_temp'] = weight_dist * (1 - filtered_data['dist_score'])
  filtered_data["readcount_score"] = weight_rc * (filtered_data["readcount_score"])
  filtered_data['congestion_score_temp'] = weight_conavg * filtered_data['congestion_score']
  filtered_data['senti_score'] = weight_sentiavg * filtered_data['senti_avg']
  filtered_data['covid_score'] = weight_covid * (1 - filtered_data['corona_score']) 
  filtered_data['star_score'] = weight_starscore * filtered_data['star_score']
  if season == 'spring' :
    filtered_data['season_score'] = weight_season * filtered_data['spring']
  elif season == 'summer' :
    filtered_data['season_score'] = weight_season * filtered_data['summer']
  elif season == 'fall' :
    filtered_data['season_score'] = weight_season * filtered_data['fall']
  else :
    filtered_data['season_score'] = weight_season * filtered_data['winter']

  # feature 합산
  try:
    result_data = tour_data.iloc[filtered_data["tour_id"]]
  except IndexError:
    return

  result_data["rank"] = filtered_data['dist_cost_temp'] + filtered_data["readcount_score"] + \
                        filtered_data["congestion_score_temp"] + filtered_data["senti_score"] + \
                        filtered_data["star_score"] + filtered_data["season_score"] + filtered_data['covid_score']

  result_data["senti"] = filtered_data["senti_word"]

  result_data[["senti","corona_score","congestion_score","star_avg","dist"]] = filtered_data[["senti_word","corona_score","congestion_score","star_avg","dist"]]
  result_data["dist"] = round(result_data["dist"],2)
  result_data['star_avg'] = round(result_data["star_avg"],1)


  result = result_data.sort_values(by=["rank"], ascending=False).head(50)
  result = result.reset_index(drop=True)

  return result