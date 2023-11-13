# 여성 패션 트렌드 분석을 위한 실시간 데이터 처리

### **📖 Contents**  

1️⃣ [프로젝트 개요](#-프로젝트-개요)   
2️⃣ [데이터 파이프라인](#-데이터-파이프라인)  
3️⃣ [데이터 프로덕트](#-데이터-프로덕트)  
4️⃣ [마무리](#-마무리)  

<br>

## 🍎 프로젝트 개요

### ✔️ 프로젝트 기간
 2023-10-30 ~ 2023-11-10

### ✔️ 주제 선정 배경
빠르게 변화하는 패션 산업에 대응하여 실시간 데이터 처리를 통해 2·30대 여성의 최신 패션 의류 트렌드를 즉각적으로 분석하고 소비자 선호에 대한 통찰력을 제공합니다.

### ✔️ 수집 데이터
- 네이버 쇼핑인사이트 : 2·30대 여성 패션 의류 일일 인기 검색어
- 네이버 블로그 키워드 검색 : 제목, 본문, 작성일자 등
- 네이버 카페 키워드 검색 : 제목, 본문, 작성일자 등
- 유튜브 검색 API : 검색 조건에 해당하는 동영상/채널/재생목록
- 유튜브 비디오 API : 동영상 목록 조회
- 유튜브 댓글 API : 동영상에 달린 댓글목록 조회

### ✔️ 기술 스택
#### ETL 파이프라인
  - 배치도구 : <img src="https://img.shields.io/badge/Airflow-017CEE?style=flat-square&logo=apacheairflow&logoColor=black">
  - 데이터 스토리지 : <img src="https://img.shields.io/badge/Amazon S3-569A31?style=flat-square&logo=amazons3&logoColor=white">
  - 실시간 데이터 스트리밍 서비스 : <img src="https://img.shields.io/badge/Amazon Kinesis-FF9900?style=flat-square&logo=amazonaws&logoColor=white">
  - 데이터 분산 처리 엔진 : <img src="https://img.shields.io/badge/Amazon EMR-FF9900?style=flat-square&logo=amazonaws&logoColor=white">
  - 검색엔진 : <img src="https://img.shields.io/badge/Elasticsearch-005571?style=flat-square&logo=elasticsearch&logoColor=white">

<br>
<br>

## 🚀 데이터 파이프라인
![aws아키텍처](https://github.com/zisu17/CloudDataPipeline/assets/108858121/cc20f2f9-a50d-4f05-89b5-77790dd0215c)
