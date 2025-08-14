# app.py
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import streamlit.components.v1 as components

# --- CSS 삽입 ---
st.markdown("""
<style>
body {
    background-color: #f4f7f9;
    color: #333;
}
.dashboard-container {
    max-width: 1200px;
    margin: auto;
    background: #fff;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}
.main-title {
    text-align: center;
    color: #2c3e50;
    margin-bottom: 30px;
}
.summary-cards {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    margin: 20px 0;
}
.card {
    background-color: #ecf0f1;
    padding: 20px;
    border-radius: 8px;
    text-align: center;
    flex: 1;
    margin: 10px;
    min-width: 200px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}
.card h3 {
    margin-top: 0;
    color: #34495e;
}
.card p {
    font-size: 2em;
    margin: 5px 0;
    font-weight: bold;
}
.chart-container {
    margin: 30px 0;
    padding: 20px;
    background: #fdfdfd;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}
</style>
""", unsafe_allow_html=True)

# 전체 대시보드 래퍼 시작
st.markdown('<div class="dashboard-container">', unsafe_allow_html=True)

# 제목
st.markdown('<h1 class="main-title">2024년 파트5 월별 매출 대시보드</h1>', unsafe_allow_html=True)

# 데이터 정의
data = [
    {"월": "2024-01", "매출액": 12000000, "증감률": 14.3},
    {"월": "2024-02", "매출액": 13500000, "증감률": 20.5},
    {"월": "2024-03", "매출액": 11000000, "증감률": -14.1},
    {"월": "2024-04", "매출액": 18000000, "증감률": 18.4},
    {"월": "2024-05", "매출액": 21000000, "증감률": 13.5},
    {"월": "2024-06", "매출액": 24000000, "증감률": 19.4},
    {"월": "2024-07", "매출액": 22500000, "증감률": 18.4},
    {"월": "2024-08", "매출액": 23000000, "증감률": 12.2},
    {"월": "2024-09", "매출액": 19500000, "증감률": 8.3},
    {"월": "2024-10", "매출액": 25000000, "증감률": 16.3},
    {"월": "2024-11", "매출액": 26500000, "증감률": 15.2},
    {"월": "2024-12", "매출액": 28000000, "증감률": 12.0}
]
df = pd.DataFrame(data)

# 요약 정보 계산
total_revenue = df["매출액"].sum()
average_growth = df["증감률"].mean()

# 요약 카드
st.markdown('<div class="summary-cards">', unsafe_allow_html=True)

st.markdown(f'''
<div class="card">
  <h3>총 매출액</h3>
  <p>{total_revenue:,.0f} 원</p>
</div>
''', unsafe_allow_html=True)

st.markdown(f'''
<div class="card">
  <h3>평균 증감률</h3>
  <p>{average_growth:.2f} %</p>
</div>
''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# --- 차트 1: 월별 매출액 추이 (라인+면적) ---
fig1 = go.Figure()
fig1.add_trace(go.Scatter(
    x=df['월'], y=df['매출액'], mode='lines',
    line=dict(color='#3498db', shape='spline', smoothing=1.3),
    fill='tonexty', fillcolor='rgba(52,152,219,0.2)',
    hovertemplate='매출액: %{y:,} 원<extra></extra>'
))
fig1.update_layout(
    showlegend=False,
    margin=dict(l=20, r=20, t=20, b=20),
    yaxis=dict(title='매출액 (원)', tickformat=','),
    plot_bgcolor='#fdfdfd', paper_bgcolor='#fdfdfd'
)

st.markdown('<div class="chart-container">', unsafe_allow_html=True)
st.markdown('### 월별 매출액 추이', unsafe_allow_html=True)
components.html(fig1.to_html(full_html=False, include_plotlyjs='cdn'), height=450)
st.markdown('</div>', unsafe_allow_html=True)

# --- 차트 2: 전년 동월 대비 증감률 (바) ---
colors = ['#2ecc71' if v >= 0 else '#e74c3c' for v in df['증감률']]
fig2 = go.Figure(go.Bar(
    x=df['월'], y=df['증감률'], marker_color=colors,
    hovertemplate='증감률: %{y:.1f} %<extra></extra>'
))
fig2.update_layout(
    showlegend=False,
    margin=dict(l=20, r=20, t=20, b=20),
    yaxis=dict(title='증감률 (%)'),
    plot_bgcolor='#fdfdfd', paper_bgcolor='#fdfdfd'
)

st.markdown('<div class="chart-container">', unsafe_allow_html=True)
st.markdown('### 월별 전년 동월 대비 증감률', unsafe_allow_html=True)
components.html(fig2.to_html(full_html=False, include_plotlyjs=False), height=450)
st.markdown('</div>', unsafe_allow_html=True)

# 대시보드 래퍼 종료
st.markdown('</div>', unsafe_allow_html=True)
