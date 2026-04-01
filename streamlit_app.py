import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="자기소개",
    page_icon="👤",
    layout="wide"
)

# ==================== 프로필 헤더 ====================
st.title("👤 나의 소개")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("백쌤 사진")
    st.info("📷 프로필 사진을 여기에 표시합니다")

with col2:
    st.subheader("기본 정보")
    
    name = st.text_input("이름", placeholder="예: 백영희", value="백영희")
    email = st.text_input("이메일", placeholder="example@email.com", value="baekyounghee@example.com")
    phone = st.text_input("전화번호", placeholder="010-1234-5678", value="010-1234-5678")
    location = st.text_input("거주지역", placeholder="예: 대한민국 서울시 강남구", value="대한민국 서울시 강남구")

st.divider()

# ==================== 자기소개 ====================
st.subheader("📝 자기소개")
introduction = st.text_area(
    "자신을 소개해주세요",
    height=180,
    value="안녕하세요! 저는 보건 분야에서 10년 이상의 경력을 가진 전문가입니다. 숙명여자대학교에서 보건학 석사를 졸업하고, 다양한 의료기관과 보건정책 분야에서 근무하며 건강관리와 의료서비스 개선에 기여해왔습니다. 데이터 분석과 인공지능 기술을 활용하여 보건 분야의 효율성을 높이는 데 관심이 많으며, 항상 환자 중심의 따뜻한 의료서비스를 추구합니다."
)

st.divider()

# ==================== 경력 및 경험 ====================
st.subheader("💼 경력 및 경험")

col1, col2 = st.columns(2)

with col1:
    st.write("**경력**")
    experience = st.number_input("경력 (년)", min_value=0, max_value=60, step=1, value=10)

with col2:
    st.write("**직급**")
    position = st.selectbox("직급", ["인턴", "사원", "주임", "대리", "과장", "부장", "이사", "기타"], index=5)

col1, col2 = st.columns(2)

with col1:
    company = st.text_input("현재/이전 회사", placeholder="회사명", value="서울대학교병원")

with col2:
    job_title = st.text_input("직무/직책", placeholder="예: 개발자, 디자이너", value="보건관리과장")

st.divider()

# ==================== 기술 스택 ====================
st.subheader("🛠️ 기술 스택")

tech_stack = st.multiselect(
    "사용 가능한 기술/언어를 선택하세요",
    ["Python", "JavaScript", "Java", "C++", "C#", "Go", "Rust", "PHP", "Ruby",
     "React", "Vue", "Angular", "Django", "Flask", "FastAPI", "Node.js",
     "SQL", "MongoDB", "PostgreSQL", "MySQL", "AWS", "GCP", "Azure",
     "Docker", "Kubernetes", "Git", "GitHub", "GitLab", "R", "SAS", "SPSS", 
     "Tableau", "Power BI", "Excel"],
    default=["Python", "SQL", "R", "SAS", "SPSS", "Tableau", "Power BI", "Excel", "Git", "GitHub"]
)

if tech_stack:
    st.write("**선택된 기술:**")
    cols = st.columns(3)
    for idx, tech in enumerate(tech_stack):
        cols[idx % 3].write(f"✓ {tech}")

st.divider()

# ==================== 교육 배경 ====================
st.subheader("🎓 교육 배경")

col1, col2 = st.columns(2)

with col1:
    education = st.selectbox("최종 학력", ["고등학교", "학사", "석사", "박사", "기타"], index=2)

with col2:
    school = st.text_input("학교명", placeholder="대학교명", value="숙명여자대학교")

major = st.text_input("전공", placeholder="예: 컴퓨터공학", value="보건")

st.divider()

# ==================== 포트폴리오 ====================
st.subheader("🎨 포트폴리오")

portfolio_count = st.number_input("포트폴리오 항목 개수", min_value=0, max_value=10, step=1, value=3)

for i in range(int(portfolio_count)):
    with st.expander(f"프로젝트 {i+1}"):
        if i == 0:
            project_name = st.text_input(f"프로젝트명", key=f"project_{i}", value="병원 환자 관리 시스템 개발")
            project_desc = st.text_area(f"프로젝트 설명", height=80, key=f"desc_{i}", 
                                      value="병원 환자 정보를 효율적으로 관리할 수 있는 웹 기반 시스템을 개발했습니다. 환자 등록, 진료 기록 관리, 약물 처방 등의 기능을 포함합니다.")
            project_url = st.text_input(f"프로젝트 링크", key=f"url_{i}", value="https://github.com/baekyounghee/patient-management")
            project_tech = st.text_input(f"사용 기술", key=f"tech_{i}", value="Python, Django, PostgreSQL, React")
        elif i == 1:
            project_name = st.text_input(f"프로젝트명", key=f"project_{i}", value="보건 데이터 분석 대시보드")
            project_desc = st.text_area(f"프로젝트 설명", height=80, key=f"desc_{i}", 
                                      value="지역별 건강지표 데이터를 분석하여 시각화하는 대시보드를 구축했습니다. 코로나19 확진자 추이, 백신 접종률 등의 정보를 실시간으로 모니터링할 수 있습니다.")
            project_url = st.text_input(f"프로젝트 링크", key=f"url_{i}", value="https://github.com/baekyounghee/health-dashboard")
            project_tech = st.text_input(f"사용 기술", key=f"tech_{i}", value="Python, Streamlit, Pandas, Plotly, SQL")
        elif i == 2:
            project_name = st.text_input(f"프로젝트명", key=f"project_{i}", value="원격 의료 상담 플랫폼")
            project_desc = st.text_area(f"프로젝트 설명", height=80, key=f"desc_{i}", 
                                      value="비대면 진료를 위한 화상 상담 플랫폼을 개발했습니다. 실시간 채팅, 화상 통화, 처방전 전송 등의 기능을 제공합니다.")
            project_url = st.text_input(f"프로젝트 링크", key=f"url_{i}", value="https://github.com/baekyounghee/telemedicine-platform")
            project_tech = st.text_input(f"사용 기술", key=f"tech_{i}", value="React, Node.js, WebRTC, MongoDB, AWS")
        else:
            project_name = st.text_input(f"프로젝트명", key=f"project_{i}")
            project_desc = st.text_area(f"프로젝트 설명", height=80, key=f"desc_{i}")
            project_url = st.text_input(f"프로젝트 링크", key=f"url_{i}")
            project_tech = st.text_input(f"사용 기술", key=f"tech_{i}")

st.divider()

# ==================== 소셜 미디어 ====================
st.subheader("🔗 소셜 미디어 및 링크")

col1, col2 = st.columns(2)

with col1:
    github = st.text_input("GitHub", placeholder="https://github.com/username", value="https://github.com/baekyounghee")
    linkedin = st.text_input("LinkedIn", placeholder="https://linkedin.com/in/username", value="https://linkedin.com/in/baekyounghee")

with col2:
    twitter = st.text_input("Twitter", placeholder="https://twitter.com/username", value="https://twitter.com/baekyounghee")
    blog = st.text_input("블로그", placeholder="https://blog.example.com", value="https://baekyounghee-healthcare.tistory.com")

st.divider()

# ==================== 취미 및 관심사 ====================
st.subheader("🎯 취미 및 관심사")

hobbies = st.multiselect(
    "관심사를 선택하세요",
    ["독서", "영화감상", "운동", "게임", "음악", "요리", "여행", "사진", "그림", "글쓰기",
     "코딩", "팟캐스트", "인공지능", "딥러닝", "데이터 분석", "요가", "기타"],
    default=["독서", "요가", "여행", "사진", "글쓰기", "데이터 분석"]
)

if hobbies:
    st.write("**선택된 관심사:**")
    st.write(", ".join(hobbies))

st.divider()

# ==================== 제출 버튼 ====================
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📤 제출", use_container_width=True):
        if name:
            st.success(f"✅ {name}님의 자기소개가 저장되었습니다!")
        else:
            st.error("❌ 이름을 입력해주세요")

with col2:
    if st.button("🔄 초기화", use_container_width=True):
        st.info("ℹ️ 페이지를 새로고침하시면 초기화됩니다")

with col3:
    if st.button("📥 다운로드", use_container_width=True):
        st.info("ℹ️ 다운로드 기능 준비 중입니다")

st.divider()

# ==================== 요약 정보 --==================
st.subheader("📋 입력 정보 요약")

if name:
    with st.container(border=True):
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("이름", name if name else "-")
        col2.metric("직급", position if position else "-")
        col3.metric("경력", f"{experience}년" if experience else "-")
        col4.metric("기술수", len(tech_stack))
else:
    st.info("📝 정보를 입력하면 요약이 표시됩니다")
