import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from haversine import haversine
from sklearn.preprocessing import MinMaxScaler


def recommend(lat,lng):
  # sql 호출, 데이터 불러오기
  engine = create_engine("mysql://admin:1234@localhost:3306/Tourlist")
  tour_data = pd.read_sql("SELECT * FROM TOURLIST_SITE", engine)
  scale_data = pd.read_sql("SELECT * FROM ANALYSIS_RESULT", engine)

  # 가중치
  weight_dist = 0.99
  weight_rc = 0.005
  weight_conavg = 0.005

  # outlier 제외 max값 산출
  iqr = tour_tmap["readcount"].quantile(.75) - tour_tmap["readcount"].quantile(.25)
  uf = tour_tmap["readcount"].quantile(.75) + (1.5 * iqr)

  # outlier 보정
  for i in range(len(tour_tmap)):
      if tour_tmap.iloc[i, tour_tmap.columns.get_loc("readcount")] > uf:
        tour_tmap.iloc[i, tour_tmap.columns.get_loc("readcount")] = 100000
  
  cur_location = (lat,lng)

  # gps 좌표로 거리(km) 계산
  scale_data["dist"] = tour_data.apply(lambda x: haversine(cur_location, (x['mapy'], x['mapx'])), axis=1)

  # 0~1 사이 값으로 scaling
  scaler = MinMaxScaler()
  scale_data[["dist_score"]] = scaler.fit_transform(scale_data[["dist"]])

  # weight 계산
  scale_data["dist_score"] = weight_dist * (1 - scale_data["dist_score"])
  scale_data["readcount_score"] = weight_rc * (scale_data["readcount_score"])
  scale_data["congestion_score"] = weight_conavg * (scale_data["congestion_score"])

  # #감성단어 추가
  # tour_data = pd.merge(left = tour_data, right = total_result[["tour_id","senti"]], how = "left", on = "tour_id")

  # feature 합산
  tour_data["rank"] = scale_data["dist_score"]+scale_data["readcount_score"]+scale_data["congestion_score"]
  tour_data["senti"] = scale_data["senti_word"]

  result = tour_data.sort_values(by=["rank"], ascending=False).head(50)
  result = result.reset_index(drop=True)

  return result