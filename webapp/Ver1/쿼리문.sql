CREATE DATABASE Tourlist CHARACTER SET UTF8;

USE Tourlist;

CREATE TABLE TOURLIST_SITE(
	tour_id INT NOT NULL,
	title VARCHAR(255) NOT NULL,
	cat1 VARCHAR(3) NOT NULL,
	cat2 VARCHAR(5) NOT NULL,
	cat3 VARCHAR(9) NOT NULL,
	areacode INT,
	addr1 VARCHAR(255),
	tel VARCHAR(31),
	mapx FLOAT(10,7) NOT NULL,
	mapy FLOAT(10,7) NOT NULL,
	firstimage VARCHAR(255),
	firstimage2 VARCHAR(255),
	contentid INT NOT NULL,
	contenttypeid INT NOT NULL,
	readcount INT,
	sigungucode INT,
	zipcode INT,
	PRIMARY KEY(tour_id)
	
)ENGINE = INNODB;


CREATE TABLE TOURLIST_TRAFFIC(
	tour_id INT NOT NULL,
	congestion_1 INT NOT NULL,
	congestion_2 INT NOT NULL,
	congestion_3 INT NOT NULL,
	congestion_4 INT NOT NULL,
	congestion_avg FLOAT NOT NULL,
	congestion_max FLOAT NOT NULL,
	road_count INT NOT NULL,
	measured_at VARCHAR(31) NOT NULL,
	FOREIGN KEY (tour_id) REFERENCES tourlist_site(tour_id),
	PRIMARY KEY(tour_id,measured_at) 
)ENGINE = INNODB;

CREATE TABLE TOURLIST_USER(
	user_id VARCHAR(31) NOT NULL,
	user_pw VARCHAR(63) NOT NULL,
	user_name VARCHAR(31) NOT NULL,
	gender VARCHAR(1) NOT NULL,
	email VARCHAR(63) NOT NULL,
	address VARCHAR(255) NOT NULL,
	gps_x FLOAT(10,7) NOT NULL,
	gps_y FLOAT(10,7) NOT NULL,
	CREATE_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY(user_id) 
)ENGINE = InnoDB;

CREATE TABLE ANALYSIS_RESULT(
	tour_id INT NOT NULL,
	readcount_score FLOAT,
	congestion_score FLOAT,
	star_avg FLOAT,
	senti_word TEXT,
	senti_count INT,
	senti_sum INT,
	senti_avg FLOAT,
	corona_score FLOAT,
	spring FLOAT,
	summer FLOAT,
	fall FLOAT,
	winter FLOAT,
	star_score FLOAT,
	FOREIGN KEY (tour_id) REFERENCES tourlist_site(tour_id),
	PRIMARY KEY(tour_id) 
)ENGINE = InnoDB;

LOAD DATA LOCAL INFILE 'C:\\bigdata2020\\data\\tour_data_bar.csv'
INTO TABLE tourlist_site
FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE 'C:/bigdata2020/data/day14/day14-all.csv'
INTO TABLE tourlist_traffic
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE 'C:\\bigdata2020\\data\\total_analysis_result.csv'
INTO TABLE analysis_result
FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

INSERT INTO TOURLIST_USER VALUES ( 'test', '1234', 'testuser','M','test@naver.com','서울특별시','126.8828','37.4798','2020/10/19');