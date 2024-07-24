import csv
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 파일 경로
file_path_avg_age = '202406_202406_주민등록인구기타현황(평균연령)_월간.csv'

# 데이터 로드
data_avg_age = pd.read_csv(file_path_avg_age, encoding='cp949')

# 데이터 전처리
data_avg_age['2024년06월_평균연령'] = data_avg_age['2024년06월_평균연령'].astype(float)

# 사용자 입력
chart_type = st.selectbox('그래프 유형을 선택하세요:', ['막대 그래프', '선 그래프', '원 그래프'])
age_criteria = st.selectbox('평균 연령 기준을 선택하세요:', ['합계', '남자', '여자'])

# 선택한 기준에 맞는 데이터 컬럼 설정
if age_criteria == '합계':
    age_column = '2024년06월_평균연령'
elif age_criteria == '남자':
    age_column = '2024년06월_평균연령_남자'
elif age_criteria == '여자':
    age_column = '2024년06월_평균연령_여자'

# 그래프 그리기
st.write(f'{age_criteria} 기준 행정구역별 평균 연령')

if chart_type == '막대 그래프':
    plt.figure(figsize=(10, 6))
    sns.barplot(x='행정구역', y=age_column, data=data_avg_age)
    plt.xticks(rotation=90)
    plt.xlabel('행정구역')
    plt.ylabel('평균 연령')
    plt.title(f'행정구역별 평균 연령 ({age_criteria})')
    st.pyplot(plt)

elif chart_type == '선 그래프':
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='행정구역', y=age_column, data=data_avg_age, marker='o')
    plt.xticks(rotation=90)
    plt.xlabel('행정구역')
    plt.ylabel('평균 연령')
    plt.title(f'행정구역별 평균 연령 ({age_criteria})')
    st.pyplot(plt)

elif chart_type == '원 그래프':
    plt.figure(figsize=(8, 8))
    plt.pie(data_avg_age[age_column], labels=data_avg_age['행정구역'], autopct='%1.1f%%', startangle=140)
    plt.title(f'행정구역별 평균 연령 비율 ({age_criteria})')
    st.pyplot(plt)

streamlit run app.py
