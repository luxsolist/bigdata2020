import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from haversine import haversine
from sklearn.preprocessing import MinMaxScaler


def recommend(lat, lng, category, dist, congestion):
  # sql 호출, 데이터 불러오기
  engine = create_engine("mysql://admin:1234@localhost:3306/Tourlist")
  tour_data = pd.read_sql("SELECT * FROM TOURLIST_SITE", engine)
  scale_data = pd.read_sql("SELECT * FROM ANALYSIS_RESULT", engine)

  # 가중치
  weight_dist = 1
  weight_rc = 1
  weight_conavg = 1

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
  filtered_data = filter_dist if congestion == 'none' else \
    filter_dist.loc[(filter_dist["congestion_score"] <= int(congestion, base=10)) & \
       (filter_dist["congestion_score"] > (int(congestion, base=10) - 1))]

  # 0~1 사이 값으로 scaling
  scaler = MinMaxScaler()
  try:
    filtered_data[["dist_score"]] = scaler.fit_transform(filtered_data[["dist"]])
  except ValueError:
    return

  # weight 계산
  filtered_data["dist_score"] = weight_dist * (1 - filtered_data["dist_score"])
  filtered_data["readcount_score"] = weight_rc * (filtered_data["readcount_score"])
  filtered_data["congestion_score"] = weight_conavg * (filtered_data["congestion_score"])

  # #감성단어 추가
  # tour_data = pd.merge(left = tour_data, right = total_result[["tour_id","senti"]], how = "left", on = "tour_id")

  # feature 합산
  try:
    result_data = tour_data.iloc[filtered_data["tour_id"]]
  except IndexError:
    return
    
  result_data["rank"] = filtered_data["dist_score"] + filtered_data["readcount_score"] + \
                        filtered_data["congestion_score"] + filtered_data["star_score"] + \
                        filtered_data["senti_avg"] + filtered_data["corona_score"]

  result_data["senti"] = filtered_data["senti_word"]
  # tour_data["rank"] = scale_data["dist_score"]+scale_data["readcount_score"]+scale_data["congestion_score"]
  # tour_data["senti"] = scale_data["senti_word"]

  result = result_data.sort_values(by=["rank"], ascending=False).head(50)
  result = result.reset_index(drop=True)
  
  return result