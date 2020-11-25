import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from haversine import haversine
from sklearn.preprocessing import MinMaxScaler
import MySQLdb
import pymysql
import MySQLdb

def batch():
    # sql 호출, 데이터 불러오기
    engine = create_engine("mysql://admin:1234@localhost:3306/Tourlist")
    tour_data = pd.read_sql("SELECT * FROM TOURLIST_SITE", engine)
    tmap_d14 = pd.read_sql("SELECT * FROM TOURLIST_SITE", engine)
    tour_data = tour_data[['tour_id', 'readcount']]
    tmap_data = tmap_d14[["tour_id", "congestion_avg"]]
    tour_tmap = pd.merge(tour_data, tmap_data, how='left', left_on="tour_id", right_on="tour_id")

    # 결측치 평균값으로 채우기 
    tour_tmap['congestion_avg'] = tour_tmap['congestion_avg'].fillna(tour_tmap['congestion_avg'].mean())

    # outlier 제외 max값 산출
    iqr = tour_tmap["readcount"].quantile(.75) - tour_tmap["readcount"].quantile(.25)
    uf = tour_tmap["readcount"].quantile(.75) + (1.5 * iqr)
    uf
    
    # outlier 보정
    for i in range(len(tour_tmap)):
        if tour_tmap.iloc[i, tour_tmap.columns.get_loc("readcount")] > uf:
            tour_tmap.iloc[i, tour_tmap.columns.get_loc("readcount")] = 100000

    # 0~1사이 값으로 scaling
    scaler = MinMaxScaler()
    scaler.fit_transform(tour_tmap[['readcount', 'congestion_avg']])
    tour_tmap[['readcount', 'congestion_avg']] = scaler.fit_transform(tour_tmap[['readcount', 'congestion_avg']])

    return tour_tmap