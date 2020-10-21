import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from haversine import haversine
from sklearn.preprocessing import MinMaxScaler

def recommend():
  # sql 호출, 데이터 불러오기
  engine = create_engine("mysql://admin:1234@localhost:3306/Tourlist")
  tour_data = pd.read_sql("SELECT * FROM TOURLIST_SITE", engine)
  tmap_d14 = pd.read_sql("SELECT * FROM TOURLIST_TRAFFIC", engine)
  tmap_data = tmap_d14[["tour_id", "congestion_avg", "measured_at"]]
  tour_tmap = pd.merge(tour_data, tmap_data, how='left', left_on="tour_id",
                       right_on="tour_id")

  # 가중치
  weight_dist = 0.8
  weight_rc = 0.15
  weight_conavg = 0.05

  # outlier 제외 max값 산출
  iqr = tour_tmap["readcount"].quantile(.75) - tour_tmap["readcount"].quantile(.25)
  uf = tour_tmap["readcount"].quantile(.75) + (1.5 * iqr)

  # outlier 보정
  for i in range(len(tour_tmap)):
      if tour_tmap.iloc[i, tour_tmap.columns.get_loc("readcount")] > uf:
        tour_tmap.iloc[i, tour_tmap.columns.get_loc("readcount")] = 100000
  
  # 위치 초기 설정
  # 이 부분은 나중에 사용자 값 or 찾고싶은 지역의 위도/경도 값 집어넣게 코딩
  cur_location = (37.3947464,127.1090181)

  # gps 좌표로 거리(km) 계산
  tour_tmap["dist"] = tour_tmap.apply(lambda x: haversine(cur_location, (x['mapy'], x['mapx'])), axis=1)

  # 0~1 사이 값으로 scaling
  scaler = MinMaxScaler()
  tour_tmap[["dist_scaled", "readcount_scaled", "conavg_scaled"]] = \
    scaler.fit_transform(tour_tmap[["dist", "readcount", "congestion_avg"]])

  # weight 계산
  tour_tmap["dist_scaled"] = weight_dist * (1 - tour_tmap["dist_scaled"])
  tour_tmap["readcount_scaled"] = weight_rc * (1 - tour_tmap["readcount_scaled"])
  tour_tmap["conavg_scaled"] = weight_conavg * (1 - tour_tmap["conavg_scaled"])

  # feature 합산
  tour_tmap["rank"] = tour_tmap["dist_scaled"] + tour_tmap["readcount_scaled"] + tour_tmap["conavg_scaled"]

  result = tour_tmap.sort_values(by=["rank"], ascending=False).head(50)

  return result