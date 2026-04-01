import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, time
import plotly.express as px

# 페이지 설정
st.set_page_config(
    page_title="Streamlit 요소 완전 가이드",
    page_icon="🎨",
    layout="wide"
)

# 제목 및 소개
st.title("🎨 Streamlit 요소들 완전 가이드")
st.markdown("Streamlit의 다양한 요소들과 위젯들을 한눈에 볼 수 있습니다!")

# 목차
st.sidebar.markdown("## 📑 목차")
page = st.sidebar.radio(
    "섹션 선택:",
    ["📝 텍스트 요소", "🎛️ 입력 위젯", "📊 데이터 표시", "📸 미디어", "📐 레이아웃", "🎯 상태 메시지"]
)

# ==================== 1. 텍스트 요소 ====================
if page == "📝 텍스트 요소":
    st.header("텍스트 요소들")
    
    with st.expander("더 알아보기", expanded=True):
        st.subheader("1. Header - 큰 제목")
        st.write("위에 보이는 것이 header입니다")
        
        st.subheader("2. Subheader - 중간 제목")
        st.write("위에 보이는 것이 subheader입니다")
        
        st.markdown("### 3. Markdown - 마크다운 포맷")
        st.markdown("""
        - **굵은 텍스트**
        - *이탤릭 텍스트*
        - `코드 블락`
        - [링크](https://streamlit.io)
        - ~~취소선~~
        """)
        
        st.divider()
        
        st.write("### 4. Write - 일반 텍스트")
        st.write("write()는 가장 유연한 텍스트 요소입니다")
        st.write("📌 여러 타입을 표시할 수 있습니다:")
        st.write(123)
        st.write({"key": "value", "숫자": 42})
        st.write([1, 2, 3, 4, 5])
        
        st.divider()
        
        st.code("""
# Python 코드 예시
def hello_world():
    print("안녕하세요, Streamlit!")
        """, language="python")
        
        st.divider()
        
        st.latex(r"e^{i\pi} + 1 = 0")

# ==================== 2. 입력 위젯 ====================
elif page == "🎛️ 입력 위젯":
    st.header("입력 위젯들")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("텍스트 입력")
        name = st.text_input("이름을 입력하세요:", placeholder="예: 김철수")
        email = st.text_area("이메일 주소:", placeholder="email@example.com")
        if name:
            st.info(f"👋 안녕하세요, {name}님!")
    
    with col2:
        st.subheader("숫자 입력")
        age = st.number_input("나이를 입력하세요:", min_value=1, max_value=120, step=1)
        height = st.slider("키(cm):", min_value=100, max_value=220, step=1)
        st.write(f"입력된 나이: {age}세, 키: {height}cm")
    
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("선택 위젯")
        checkbox = st.checkbox("동의합니다", value=False)
        st.write(f"체크박스 상태: {checkbox}")
        
        option = st.radio("선택하세요:", ["선택지 1", "선택지 2", "선택지 3"])
        st.write(f"선택된 것: {option}")
    
    with col2:
        st.subheader("드롭다운 및 다중선택")
        city = st.selectbox("도시 선택:", ["서울", "부산", "대구", "인천", "광주"])
        st.write(f"선택된 도시: {city}")
        
        hobbies = st.multiselect(
            "취미를 선택하세요(복수):",
            ["독서", "영화감상", "운동", "게임", "음악", "요리"]
        )
        st.write(f"선택된 취미: {hobbies}")
    
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("날짜 및 시간")
        date = st.date_input("날짜 선택:", value=datetime.today())
        st.write(f"선택된 날짜: {date}")
    
    with col2:
        st.subheader("시간 선택")
        time_input = st.time_input("시간 선택:", value=time(12, 0))
        st.write(f"선택된 시간: {time_input}")
    
    st.divider()
    
    st.subheader("버튼 및 폼")
    col1, col2, col3 = st.columns(3)
    
    if col1.button("🔘 클릭 버튼", use_container_width=True):
        st.success("버튼을 클릭했습니다!")
    
    if col2.button("❌ 다른 버튼", use_container_width=True):
        st.warning("이 버튼도 클릭 가능합니다!")
    
    if col3.download_button(
        "⬇️ 파일 다운로드",
        data="Hello Streamlit",
        file_name="sample.txt",
        use_container_width=True
    ):
        st.info("파일 다운로드됨")
    
    st.subheader("폼 (Form)")
    with st.form("my_form"):
        st.write("폼 내부 입력:")
        form_name = st.text_input("이름:")
        form_age = st.slider("나이:", 1, 100)
        form_submitted = st.form_submit_button("제출")
        
        if form_submitted:
            st.write(f"제출되었습니다: {form_name}, {form_age}세")

# ==================== 3. 데이터 표시 ====================
elif page == "📊 데이터 표시":
    st.header("데이터 표시 요소들")
    
    # 샘플 데이터 생성
    df = pd.DataFrame({
        "이름": ["서울", "부산", "대구", "인천", "광주"],
        "인구": [9776000, 3404000, 2444000, 2886000, 1457000],
        "면적(km²)": [605.2, 765.8, 884.2, 1061.8, 501.3],
        "GDP(조원)": [914, 330, 248, 285, 180]
    })
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Dataframe 표시")
        st.dataframe(df, use_container_width=True, height=300)
    
    with col2:
        st.subheader("테이블 표시")
        st.table(df)
    
    st.divider()
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="총 인구", value="1,996만명", delta="↑ 2.3%")
    
    with col2:
        st.metric(label="평균 면적", value="843km²", delta="↓ 1.2%")
    
    with col3:
        st.metric(label="총 GDP", value="1,957조원", delta="↑ 5.8%")
    
    st.divider()
    
    st.subheader("JSON 데이터")
    json_data = {"서울": {"인구": 977, "GDP": 914}, "부산": {"인구": 340, "GDP": 330}}
    st.json(json_data)
    
    st.divider()
    
    st.subheader("차트")
    col1, col2 = st.columns(2)
    
    with col1:
        fig1 = px.bar(df, x="이름", y="인구", title="도시별 인구")
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        fig2 = px.pie(df, names="이름", values="GDP", title="도시별 GDP")
        st.plotly_chart(fig2, use_container_width=True)

# ==================== 4. 미디어 ====================
elif page == "📸 미디어":
    st.header("미디어 요소들")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("이미지 표시")
        st.image("https://emoji.aranja.com/static/emoji-data/img-apple-160/1f308.png", 
                width=200, caption="Streamlit 로고")
    
    with col2:
        st.subheader("이미지 컬럼 옵션")
        images = {
            "🎨": "https://emoji.aranja.com/static/emoji-data/img-apple-160/1f308.png",
            "🎈": "https://emoji.aranja.com/static/emoji-data/img-apple-160/1f388.png",
            "🎉": "https://emoji.aranja.com/static/emoji-data/img-apple-160/1f389.png",
        }
        for name, url in images.items():
            st.image(url, width=100, caption=name)

# ==================== 5. 레이아웃 ====================
elif page == "📐 레이아웃":
    st.header("레이아웃 요소들")
    
    st.subheader("1. 컬럼 (Columns)")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("컬럼 1\n너비가 동일합니다")
    with col2:
        st.success("컬럼 2\n자동 배치됩니다")
    with col3:
        st.warning("컬럼 3\n3개 열 레이아웃")
    
    st.divider()
    
    st.subheader("2. 비율을 지정한 컬럼")
    col1, col2, col3 = st.columns([2, 3, 1])
    with col1:
        st.info("비율 2")
    with col2:
        st.success("비율 3 (가장 넓음)")
    with col3:
        st.warning("비율 1 (가장 좁음)")
    
    st.divider()
    
    st.subheader("3. 탭 (Tabs)")
    tab1, tab2, tab3 = st.tabs(["탭 1️⃣", "탭 2️⃣", "탭 3️⃣"])
    
    with tab1:
        st.write("첫 번째 탭 내용")
        st.info("탭을 클릭하면 콘텐츠가 변경됩니다")
    
    with tab2:
        st.write("두 번째 탭 내용")
        st.success("각 탭은 독립적인 상태를 유지합니다")
    
    with tab3:
        st.write("세 번째 탭 내용")
        st.warning("탭은 강력한 레이아웃 도구입니다")
    
    st.divider()
    
    st.subheader("4. 확장기 (Expander)")
    with st.expander("더 보기 🔽"):
        st.write("숨겨진 콘텐츠입니다")
        st.code("st.expander('제목')")
    
    with st.expander("추가 정보"):
        st.write("이것도 숨겨진 콘텐츠입니다")
    
    st.divider()
    
    st.subheader("5. 컨테이너")
    with st.container(border=True):
        st.write("경계가 있는 컨테이너")
        st.button("컨테이너 내 버튼")

# ==================== 6. 상태 메시지 ====================
elif page == "🎯 상태 메시지":
    st.header("상태 메시지들")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("긍정/정보 메시지")
        st.success("✅ 성공! 작업이 완료되었습니다")
        st.info("ℹ️ 정보: 알아두면 좋은 정보입니다")
    
    with col2:
        st.subheader("주의/오류 메시지")
        st.warning("⚠️ 주의: 주의가 필요합니다")
        st.error("❌ 오류: 문제가 발생했습니다")
    
    st.divider()
    
    st.subheader("진행 상황 표시")
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("Progress Bar:")
        progress_bar = st.progress(0)
        for i in range(101):
            progress_bar.progress(i)
    
    with col2:
        st.write("Spinner:")
        with st.spinner("로딩 중..."):
            import time
            time.sleep(2)
        st.success("완료!")
    
    st.divider()
    
    st.subheader("예외 메시지")
    st.write("예외 정보를 표시할 수 있습니다:")
    try:
        result = 1 / 0
    except ZeroDivisionError as e:
        st.exception(e)

st.divider()
st.markdown("---")
st.write("💡 **팁**: Streamlit은 Python 파일이 수정되면 자동으로 새로고침됩니다!")
st.write("📚 [공식 문서](https://docs.streamlit.io/)에서 더 많은 정보를 얻을 수 있습니다.")
